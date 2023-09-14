from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from.models import EventUser
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
     return render(request,'Gallery.html')


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


# from django.shortcuts import render
# from django.http import HttpResponseBadRequest
# from datetime import datetime
# from .models import TimeSlot

# def booking_time(request):
#     # Get the date parameter from the URL
#     date_str = request.GET.get('date')
    
#     # Validate and parse the date string into a datetime object
#     try:
#         booking_date = datetime.strptime(date_str, '%B %d, %Y')
#     except ValueError:
#         return HttpResponseBadRequest("Invalid date format in the URL")

#     # Query TimeSlot objects based on the booking_date
#     time_slots = TimeSlot.objects.filter(is_active=True)

#     # Pass the time_slots and booking_date to the template
#     return render(request, 'GuestBooking/booking_time.html', {'time_slots': time_slots, 'booking_date': booking_date})


# # *************booking form views in guest booking*****************
# from django.shortcuts import render, redirect
# from .models import Booking
# from django.contrib import messages

# def booking(request):
#     if request.method == "POST":
#         client_name = request.POST.get('client-name')
#         client_email = request.POST.get('client-email')
#         client_phone = request.POST.get('client-phone', '')
#         booking_date = request.POST.get('booking_date')
#         booking_time = request.POST.get('booking_time')

#         # Create a new Booking instance and save it to the database
#         booking = Booking(
#             client_name=client_name,
#             client_email=client_email,
#             client_phone=client_phone,
#             booking_date=booking_date,
#             booking_time=booking_time,
#         )
#         booking.save()

#         # Add a success message
#         messages.success(request, 'Booking successful!')
        
#         # Redirect to the home page or any other appropriate page
#         return redirect('index')  

#     return render(request, 'GuestBooking/booking.html')

# from django.shortcuts import render, redirect
# from .forms import BookingForm1, BookingForm2, BookingForm3

# def Guestbooking(request):
    
#     if request.method == 'POST':
#         form1 = BookingForm1(request.POST)
#         form2 = BookingForm2(request.POST)
#         form3 = BookingForm3(request.POST)

#         if form3.is_valid():
#             Booking.date = form1.cleaned_data['date']
#             Booking.time_slot=form2.cleaned_data['time_slot']
#             Booking.client_name = form3.cleaned_data['client_name']
#             Booking.client_email = form3.cleaned_data['client_email']
#             Booking.client_phone = form3.cleaned_data['client_phone']
#             Booking.save()
#             return redirect('index')

#     else:
#         form1 = BookingForm1()
#         form2 = BookingForm2()
#         form3 = BookingForm3()

#     context = {
#         'form1': form1,
#         'form2': form2,
#         'form3': form3,
#     }
#     return render(request, 'Guestbooking.html', context)

# from django.shortcuts import render, redirect

# from .forms import BookingForm

# def Guestbooking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to a success page or do something else
#             return redirect('RegistrationSucess')
#     else:
#         form = BookingForm()

#     return render(request, 'Guestbooking.html', {'form': form})






from django.contrib.auth.decorators import login_required  # Import the login_required decorator
# Use the login_required decorator to ensure the user is logged in
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile_Verification
from django.contrib.auth.decorators import login_required
 

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

# Rest of your code remains the same# views.py guestbooking
# from django.shortcuts import render, redirect
# from .models import Booking
# from datetime import timedelta 
# def Guestbooking(request):
#     if request.method == 'POST':
#         client_name = request.POST.get('client_name')
#         client_email = request.POST.get('client_email')
#         client_phone = request.POST.get('client_phone')
#         booking_date = request.POST.get('booking_date')
#         booking_time = request.POST.get('booking_time')

#         # Process the booking request and save it to the database
#         if client_name and client_email and booking_date and booking_time:
#             # Save the booking to the database
#             Booking.objects.create(
#                 start_time=booking_time,
#                 end_time=(booking_time + timedelta(hours=1)),
#                 date=booking_date
#             )

#             # Handle the rest of your booking logic here

#             return render(request, 'booking_success.html', {'client_name': client_name})

#     return render(request, 'Guestbooking.html')

# from django.shortcuts import render, redirect
# from .models import Booking
# from datetime import datetime, timedelta  # Import datetime

# def Guestbooking(request):
#     if request.method == 'POST':
#         client_name = request.POST.get('client-name')
#         client_email = request.POST.get('client-email')
#         client_phone = request.POST.get('client-phone')
#         booking_date = request.POST.get('booking-date')
#         booking_time = request.POST.get('booking-time')

#         # Process the booking request and save it to the database
#         if client_name and client_email and booking_date and booking_time:
#             # Parse the booking date and time
#             booking_datetime = datetime.strptime(f"{booking_date} {booking_time}", "%Y-%m-%d %I:%M%p")

#             # Calculate end time (assuming each booking lasts for 1 hour)
#             end_time = booking_datetime + timedelta(hours=1)

#             # Save the booking to the database
#             Booking.objects.create(
#                 client_name=client_name,
#                 client_email=client_email,
#                 client_phone=client_phone,
#                 booking_date=booking_datetime.date(),
#                 booking_start_time=booking_datetime.time(),
#                 booking_end_time=end_time.time()
#             )

#             # Handle the rest of your booking logic here

#             return render(request, 'booking_success.html', {'client_name': client_name})

#     return render(request, 'Guestbooking.html')


from django.shortcuts import render, redirect
from .models import Booking
from datetime import datetime, timedelta  # Import datetime


def Guestbooking(request):
    if request.method == "POST":
        client_name = request.POST.get("client-name")
        print(client_name)
        client_email = request.POST.get("client-email")
        print(client_email)
        client_phone = request.POST.get("client-phone")
        print(client_phone)
        booking_date = request.POST.get("booking-date")
        print(booking_date)
        booking_time = request.POST.get("booking-time")
        print(booking_time)

        # Process the booking request and save it to the database

        # Your this condition is not matching..........🫵
        if client_name and client_email and booking_date and booking_time:
            # Parse the booking date and time
            # Split the time range into start and end times
            start_time, end_time = booking_time.split(" - ")

            # Create a datetime object for the booking date
            booking_datetime = datetime.strptime(booking_date, "%B %Y")

            # Add the start time to the datetime
            booking_datetime = booking_datetime.replace(
                hour=int(start_time.split(":")[0]),
                minute=int(start_time.split(":")[1][:-2]),  # Remove 'AM' or 'PM'
            )

            print("Booking datetime start:", booking_datetime)

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
