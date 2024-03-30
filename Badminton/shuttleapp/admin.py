from django.contrib import admin

# Register your models here.
from .models import EventUser,Profile_Verification,Booking,Winner,Trainer,TrainingRegistration,TrainingVideo
admin.site.register(EventUser)
# Register your models here.

admin.site.register(Profile_Verification)
admin.site.register(Booking)
admin.site.register(Winner)
admin.site.register(Trainer)
admin.site.register(TrainingRegistration)
admin.site.register(TrainingVideo)
