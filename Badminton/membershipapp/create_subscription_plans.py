from membershipapp.models import SubscriptionPlan

# Create a Basic plan instance
basic_plan = SubscriptionPlan.objects.create(
    title="Basic",
    price=10.00,
    duration="Monthly",
    features="Access to courts\nNo equipment rental\nBasic coaching\n24/7 service"
)

# Create other instances similarly...
# Create a Basic plan instance

# Create a Standard plan instance
standard_plan = SubscriptionPlan.objects.create(
    title="Standard",
    price=25.00,
    duration="Monthly",
    features="Access to courts\nBasic equipment rental\nIntermediate coaching\n24/7 service"
)

# Create a Premium plan instance
premium_plan = SubscriptionPlan.objects.create(
    title="Premium",
    price=50.00,
    duration="Monthly",
    features="Access to courts\nFull equipment rental\nAdvanced coaching\n24/7 service"
)
