from django.contrib import admin
from .models import CustomUser
# Register your models here.
admin.site.register(CustomUser)
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)