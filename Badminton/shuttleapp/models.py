from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from loginapp.models import CustomUser
# # Create your models here.



# Create your models here.
class EventUser(models.Model):
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
     
    
     
    def __str__(self):    
        return self.name
    

class Registration(models.Model):
    event = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=10)  # 'single' or 'team'
    name1 = models.CharField(max_length=100)
    dob1 = models.DateField()
    name2 = models.CharField(max_length=100, blank=True, null=True)
    dob2 = models.DateField(blank=True, null=True)
    contact_number = models.CharField(max_length=15)
    declaration_accepted = models.BooleanField(default=False)
    def __str__(self):
        return f'Registration for {self.event.name}'




# # Create your models here.
# from django.contrib.auth.models import User

# # class UserProfile(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     address = models.CharField(max_length=255)
# #     # Other fields for user profile

# #     def __str__(self):
# #         return self.user.username
    


# class Event(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE,default=None)
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     location = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='img/', null=True, blank=True)
    
#     def __str__(self):
#         return self.name



# #***************************guest booking time slots********************8
# from django.db import models

# class TimeSlot(models.Model):
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     capacity = models.PositiveIntegerField(default=4)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.start_time.strftime('%I:%M%p')} - {self.end_time.strftime('%I:%M%p')}"

#     def is_full(self):
#         return self.capacity <= 0


# # *************booking form models in guest booking*****************
# from django.db import models

# class Booking(models.Model):
#     client_name = models.CharField(max_length=255)
#     client_email = models.EmailField()
#     client_phone = models.CharField(max_length=15, blank=True, null=True)
#     booking_date = models.DateField()
#     booking_time = models.TimeField()

#     def __str__(self):
#         return f"Booking by {self.client_name} on {self.booking_date} at {self.booking_time}"


# class Booking(models.Model):
#     date = models.DateField()
#     time_slot = models.CharField(max_length=20,null=True)
#     client_name = models.CharField(max_length=100)
#     client_email = models.EmailField()
#     client_phone = models.CharField(max_length=15)

#     def __str__(self):
#         return f"{self.date} - {self.time_slot} - {self.client_name}"




#verify profile
from django.db import models
from django.conf import settings  # Import the settings module

# 
from django.db import models

from django.db import models

class Profile_Verification(models.Model):
    CATEGORY_CHOICES = [
        ('adhar', 'Adhar card'),
        ('passport', 'Passport'),
        ('driving_license', 'Driving License'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='adhar')
    image = models.ImageField(upload_to='images/', default='img1.jpg')

    def __str__(self):
        return self.name

    # models.py guestbooking
from django.db import models

class Booking(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=15, blank=True, null=True)
    booking_date = models.DateField()
    booking_start_time = models.TimeField()
    booking_end_time = models.TimeField()

    def __str__(self):
        return self.client_name
