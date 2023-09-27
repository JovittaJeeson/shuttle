from django.shortcuts import render

# Create your views here.


from .models import SubscriptionPlan
def membership(request):
    subscription_plans = SubscriptionPlan.objects.all()


    # Preprocess the data: Split plan.features by newline
    for plan in subscription_plans:
        plan.features = plan.features.split('\n')


    return render(request, 'membership.html', {'subscription_plans': subscription_plans})
# def membership(request):
#     subscription_plans = SubscriptionPlan.objects.all()
#     return render(request, 'membership.html', {'subscription_plans': subscription_plans})
# def membership(request, plan_id):
#     plan = SubscriptionPlan.objects.get(pk=plan_id)

#     # Split the features text into a list using newline characters
#     features_list = plan.features.split('\n')

#     context = {
#         'plan': plan,
#         'features_list': features_list,
#     }

#     return render(request, 'membership.html', context)
# payment

from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
 
 
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def Payment(request,member_id):
    member=SubscriptionPlan.objects.get(pk=member_id)
    currency = 'INR'
    amount = int(member.price)*100   # Rs. 200

 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
    # callback_url = 'membership'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'Payment.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'booking_success.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'booking_error.html')
            else:
 
                # if signature verification fails.
                return render(request, 'booking_error.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()

   


