from django.contrib import admin

# Register your models here.

from .models import SubscriptionPlan,Payment_mem
# Register your models here.
admin.site.register(SubscriptionPlan)
admin.site.register(Payment_mem)