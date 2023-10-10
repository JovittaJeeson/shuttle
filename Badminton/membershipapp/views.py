from django.shortcuts import render

# Create your views here.


from .models import SubscriptionPlan
def membership(request):
    subscription_plans = SubscriptionPlan.objects.all()


    # Preprocess the data: Split plan.features by newline
    for plan in subscription_plans:
        plan.features = plan.features.split('\n')


    return render(request, 'membership.html', {'subscription_plans': subscription_plans})

# payment

from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
 
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def Payment(request,member_id):
    member=SubscriptionPlan.objects.get(pk=member_id)
    currency = 'INR'
    amount = int(member.price)*100 # Rs. 200
#
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymenthandler/'
    
    payment_instance = Payment_mem.objects.create(
        user=request.user,
        subscription_plan=member,  
        razorpay_order_id=razorpay_order_id,
        amount=amount/100,
        status='1'
    )
    # we need to pass these details to frontend.
    context = {}
    context['amount'] = amount*100
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'Payment.html', context=context)
 
from django.shortcuts import redirect

# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
    # Only accept POST request.
    if request.method == "POST":
            # Get the required parameters from the POST request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # Verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                    # Get the Payment_mem instance associated with the payment
                    payment_instance = Payment_mem.objects.get(razorpay_order_id=razorpay_order_id)

                    # Capture the payment using the correct amount from the Payment_mem instance
                    amount = int(payment_instance.amount)
                    print(amount)
                    razorpay_client.payment.capture(payment_id, amount*100)

                    # Redirect to 'membership.html' upon successful payment capture
                    ...
                    return redirect('membership')


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Payment_mem
from .models import SubscriptionPlan, CustomUser  # Replace 'your_app' with the actual name of your app

def create_payment(request, subscription_plan_id):
    # Get the SubscriptionPlan and CustomUser instances
    subscription_plan = get_object_or_404(SubscriptionPlan, pk=subscription_plan_id)
    user = get_object_or_404(CustomUser)

    # You can customize the amount based on your requirements     , pk=user_id
    amount = subscription_plan.price

    # Create a Payment_mem instance
    payment = Payment_mem(
        subscription_plan=subscription_plan,
        user=user,
        # payment_id='your_payment_id',  # You should replace this with the actual payment ID
        amount=amount,
        status='Pending'
    )

    # Save the payment instance to the database
    payment.save()

    # You can customize the response based on your requirements
    return HttpResponse(f"Payment created successfully for {subscription_plan.title}.")
