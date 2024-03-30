from django.db import models
from loginapp.models import CustomUser

class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)
    # features = models.TextField()
    features = models.TextField(help_text="Enter each feature on a new line")
    deleted = models.BooleanField(default=False)  # Add the 'deleted' field

    def __str__(self):
        return self.title
    
class Payment_mem(models.Model):
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    razorpay_order_id = models.CharField(max_length=255,default=None)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=1, choices=(('0', 'Deactivated'), ('1', 'Activated')), default='1')

    def __str__(self):
        return f"Payment for {self.subscription_plan.title}"


#do this also bro if i subscribed i need to see who subscribed ! in admin panal ! also booking . 
    
#i think that is simple . i will pay 500 . after only u do work ...wait a sec bro balance 500 wait mujhe code ka bta do kaha par hai apke apne pc ke sath kya kar rakha h 


