from django.db import models

# # Create your models here.
# class MembershipPlan(models.Model):
#     title = models.CharField(max_length=100)  # Example: "STARTER"
#     price = models.DecimalField(max_digits=8, decimal_places=2)  # Example: 1000.00
#     duration = models.CharField(max_length=50)  # Example: "/Monthly"
#     features = models.TextField()  # Features represented as HTML

#     def __str__(self):
#         return self.title
#     from django.db import models

class SubscriptionPlan(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)
    # features = models.TextField()
    features = models.TextField(help_text="Enter each feature on a new line")
    deleted = models.BooleanField(default=False)  # Add the 'deleted' field

    def __str__(self):
        return self.title