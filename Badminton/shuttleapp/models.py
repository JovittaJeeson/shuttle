
# # Create your models here.


from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from loginapp.models import CustomUser
from django.utils import timezone

# # Create your models here.


# Create your models here.
class EventUser(models.Model):
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()  # 15 sep 2023
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    close_event_date = models.DateField(null=True, blank=True)  # 2023-09-13
    max_registrations = models.PositiveIntegerField(default=100)  # Maximum registrations allowed
    # current_registrations = models.PositiveIntegerField(default=0)  # Current registrations null=True, blank=True
    current_registrations = models.PositiveIntegerField(null=True, blank=True)
    accept_status = models.BooleanField(default=False, help_text="Accept Status")
    reject_status = models.BooleanField(default=False, help_text="Reject Status")
    org_user=models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    @property
    def is_event_closed(self):
        if self.close_event_date:
            current_date = timezone.now().date()
            return current_date >= self.close_event_date
        return True

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


#gallery  page
from django.db import models

class Winner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='winners/')
    name = models.CharField(max_length=100)
    prize = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# models.py

from django.db import models

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


# models.py

from django.db import models

class TrainingRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    game_level = models.CharField(max_length=20)
    dob = models.DateField()

from django.db import models

class TrainingVideo(models.Model):
    title = models.CharField(max_length=100)
    trainer = models.CharField(max_length=100)  # Assuming the trainer's name is stored as a CharField
    video_file = models.FileField(upload_to='training_videos/')  # Assuming the video file is uploaded as a file

    def __str__(self):
        return self.title





from django.db import models
from .models import CustomUser

class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    can_id = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE)
    status = models.BooleanField('status', default=True) 
    feedback = models.TextField(null=True)
    percentage = models.FloatField(blank=True, null=True)
    good = models.BooleanField('good', default=True)
    bad = models.BooleanField('bad', default=True)
    neutral = models.BooleanField('neutral', default=True)
    rating = models.CharField(max_length=100,null=True)

    @property
    def username(self):
        return self.can_id.name
