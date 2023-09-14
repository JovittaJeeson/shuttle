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