# In signals.py

from django.contrib.auth.models import Group
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from ecom.models import Customer

@receiver(user_logged_in)
def add_to_customer_group(sender, user, request, **kwargs):
    try:
        # Try to retrieve the associated Customer instance
        customer = Customer.objects.get(user=user)
    except Customer.DoesNotExist:
        # If the Customer instance does not exist, create one
        customer = Customer.objects.create(user=user)

    # Check if the user is already in the CUSTOMER group
    if not user.groups.filter(name='CUSTOMER').exists():
        # If not, add the user to the CUSTOMER group
        customer_group, created = Group.objects.get_or_create(name='CUSTOMER')
        user.groups.add(customer_group)
