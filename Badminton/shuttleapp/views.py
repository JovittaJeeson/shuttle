from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from.models import EventUser,Winner
# from .forms import BookingForm1,BookingForm2,BookingForm3
# Create your views here.
def index(request):
     return render(request,'index.html')
def about(request):
     return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')
def event_index(request):
     return render(request,'event_index.html')
def payment(request):
     return render(request,'payment.html')
def Event_On_Trend(request):
     eventUser=EventUser.objects.filter(status=0)
     return render(request,'Event_On_Trend.html',{"eventUser":eventUser})

def add_event(request):
     return render(request,'add_event.html')
def EventRegform(request):
     return render(request,'EventRegform.html')
def Guestbooking(request):
     return render(request,'Guestbooking.html')




def Gallery(request):
    # Query the database to get all Winner objects
    winners = Winner.objects.all()
    # Render the gallery page template and pass the winners data to it
    return render(request, 'Gallery.html', {'winners': winners})

from django.shortcuts import render, redirect, get_object_or_404
from .models import EventUser, Registration
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def EventRegform(request, event_id):
     event = get_object_or_404(EventUser, id=event_id)
     if request.method == 'POST':
          registration_type = request.POST.get('registration-type')
        
          name1 = request.POST.get('single-name') if registration_type == 'single' else request.POST.get('team-name1')
          dob1 = request.POST.get('single-dob') if registration_type == 'single' else request.POST.get('team-dob1')
          name2 = request.POST.get('team-name2') if registration_type == 'team' else None
          dob2 = request.POST.get('team-dob2') if registration_type == 'team' else None
          contact_number = request.POST.get('contact-number')
          declaration_accepted = 'declaration-checkbox' in request.POST
          print(registration_type)
        # Check if registration_type is not empty
          if not registration_type:
               messages.error(request, 'Registration type is required.')
               return redirect('EventRegform', event_id=event_id)

          registration = Registration(
               event=event,
               registration_type=registration_type,
               name1=name1,
               dob1=dob1,
               name2=name2,
               dob2=dob2,
               contact_number=contact_number,
               declaration_accepted=declaration_accepted,
          )
          registration.save()

          messages.success(request, 'Registration successfully submitted.')
          return redirect('RegistrationSucess')  # Redirect to a success page

     return render(request, 'EventRegform.html', {'event': event})




def RegistrationSucess(request):
    return render(request, 'RegistrationSucess.html')


def refere(request):
     return render(request,'refere.html')



# #add event
# from django.shortcuts import render, redirect
# from .models import EventUser

# def create_event(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         location = request.POST.get('location')
#         image = request.FILES.get('image')  # Uploaded image file

#         # Create an EventUser instance and save it to the database
#         event_user = EventUser()
#         event_user.name = name
#         event_user.description = description
#         event_user.date = date
#         event_user.time = time
#         event_user.location = location
#         event_user.image = image
#         event_user.save()

#         return redirect('Event_On_Trend')  # Redirect to a view displaying the list of events

#     return render(request, 'add_event.html')


# from django.shortcuts import render, HttpResponse
# from .models import Event
# from django.contrib.auth.decorators import login_required

# def add_event(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         location = request.POST.get('location')
#         image = request.FILES.get('image')

#         # Find the last event's ID, and increment by 1 to get the new event's ID
#         last_event = Event.objects.last()
#         if last_event:
#             event_id = last_event.id + 1
#         else:
#             event_id = 1

#         new_event = Event(
#             id=event_id,  # Set the event ID
#             user=request.user,
#             name=name,
#             description=description,
#             date=date,
#             time=time,
#             location=location,
#             image=image
#         )
#         new_event.save()
#      #    sucess_message = 'Event added successfully'
#         return HttpResponse('Event added successfully.')

#     return render(request, 'add_event.html'  )


# from django.shortcuts import render
# from .models import Event # Import your Event model

# def show_events(request):
#     events = Event.objects.all()  # Get all events from the database
#     context = {
#         'events': events,  # Pass the events to the template context
#     }
#     return render(request, 'Event_On_Trend.html', context)

#************************guset booking time slots*************************************
# from django.shortcuts import render
# from .models import TimeSlot

# def booking_time(request):
#     time_slots = TimeSlot.objects.filter(is_active=True)
    
#     return render(request, 'GuestBooking/booking_time.html', {'time_slots': time_slots})






# from django.contrib.auth.decorators import login_required  # Import the login_required decorator
# # Use the login_required decorator to ensure the user is logged in
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Profile_Verification
# from django.contrib.auth.decorators import login_required
 

from .models import Profile_Verification
from django.shortcuts import render, redirect
from django.http import HttpResponse

def ProfileVerification(request):
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        category = request.POST.get('category')
        destination_image = request.FILES['destination_image']

        new_destination = Profile_Verification(
            name=destination_name,
            category=category,
            image=destination_image,
        )
        new_destination.save()
        return redirect('RegistrationSucess')  # Redirect to a success page URL

    return render(request, 'ProfileVerification.html')  # Render the 'ProfileVerification.html' template


from django.shortcuts import render, redirect
from .models import Booking
from datetime import datetime, timedelta  # Import datetime


def Guestbooking(request):
    if request.method == "POST":
        client_name = request.POST.get("client-name")
        client_email = request.POST.get("client-email")
        print(client_email)
        booking_date = request.POST.get("booking-date")
        booking_time = request.POST.get("booking-time")

        if client_name and client_email and booking_date and booking_time:
            # Split the time range into start and end times
            start_time, end_time = booking_time.split(" - ")

            # Create a datetime object for the booking date
            booking_datetime = datetime.strptime(booking_date, "%B %Y")

            # Add the start time to the datetime
            booking_datetime = booking_datetime.replace(
                hour=int(start_time.split(":")[0]),
                minute=int(start_time.split(":")[1][:-2]),  # Remove 'AM' or 'PM'
            )

            # Now, create another datetime object for the end time
            end_datetime = booking_datetime.replace(
                hour=int(end_time.split(":")[0]),
                minute=int(end_time.split(":")[1][:-2]),  # Remove 'AM' or 'PM'
            )

            print("Booking datetime end:", end_datetime)

            # Calculate end time (assuming each booking lasts for 1 hour)
            end_time = booking_datetime + timedelta(hours=1)

            # Save the booking to the database

            Booking.objects.create(
                client_name=client_name,
                client_email=client_email,
                client_phone=client_phone,
                booking_date=booking_datetime.date(),
                booking_start_time=booking_datetime.time(),
                booking_end_time=end_time.time(),
            )

            # Handle the rest of your booking logic here

            return render(request, "booking_success.html", {"client_name": client_name})

    return render(request, "Guestbooking.html")

#gallery page

from django.shortcuts import render, redirect
from .models import Winner

def Gallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        prize = request.POST.get('prize')
        image = request.FILES['image']
        
        new_winner = Winner(
            title=title,
            name=name,
            prize=prize,
            image=image,
        )
        new_winner.save()
        return redirect('Gallery')  # You can specify the URL name you want to redirect to
    
    return render(request, 'Gallery.html')  # Replace 'add_winner.html' with your template name
