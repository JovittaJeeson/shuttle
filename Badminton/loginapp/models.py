from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from datetime import datetime

# In your models.py or any appropriate file


# @receiver(user_logged_in)
# def add_to_customer_group(sender, user, request, **kwargs):
#     # Check if the user is already in the CUSTOMER group
#     if not user.groups.filter(name='CUSTOMER').exists():
#         # If not, add the user to the CUSTOMER group
#         customer_group, created = Group.objects.get_or_create(name='CUSTOMER')
#         user.groups.add(customer_group)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    username = None
    name = models.CharField(max_length=100, default='')   
    birth = models.DateField(default=datetime.now, null=True) 
    email = models.EmailField(unique=True)    
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=12,default='')
    gender = models.CharField(max_length=128)   
    is_customer = models.BooleanField(default=False)
    is_refere = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = []   
    
    objects = CustomUserManager()
    
    def __str__(self):    
        return self.email

# Set the unique attribute of the email field to True
CustomUser._meta.get_field("email")._unique = True


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255, blank=True)  # New field for address

    def __str__(self):
        return self.user.name
