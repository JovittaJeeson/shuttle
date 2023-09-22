from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class CustomUser(AbstractUser):
    username=None
    USERNAME_FIELD = 'email'
    # username=models.CharField(max_length=100,default='',unique=True)
     # manager = models.CharField(max_length=100, default='') 
    name = models.CharField(max_length=100, default='')   
    birth = models.DateField(default=datetime.now) 
    email = models.EmailField(unique=True)    
    password = models.CharField(max_length=128) 
    phone =   models.CharField(max_length=12,default='')
    gender = models.CharField(max_length=128)   
    is_customer = models.BooleanField(default=False)
    is_refere = models.BooleanField(default=False)
    
    
    REQUIRED_FIELDS = []   
    def __str__(self):    
        return self.name




class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional profile fields here, e.g., profile picture, bio, etc.
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    # bio = models.TextField(max_length=500, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.user.name
# models.py
# from django.contrib.auth.models import User
# from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=255)
#     date_of_birth = models.DateField(null=True, blank=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True)

#     def __str__(self):
#         return self.user.username


