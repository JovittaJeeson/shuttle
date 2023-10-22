from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import EventUser,Winner,Registration,CustomUser,Winner,Booking
from loginapp.models import CustomUser
from membershipapp.models import SubscriptionPlan
from django.shortcuts import render, redirect
from membershipapp.models import SubscriptionPlan
from django.http import HttpResponse
from shuttleapp.models import Winner
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from .models import EventUser, Registration
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


from django.shortcuts import get_object_or_404, redirect
from .models import EventUser


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
# def payment(request):
#      return render(request,'payment.html')
def Event_On_Trend(request):
     eventUser=EventUser.objects.filter(status=0)
     return render(request,'Event_On_Trend.html',{"eventUser":eventUser})

from django.shortcuts import render
from .models import EventUser  # Import your EventUser model here


from django.shortcuts import render, redirect, get_object_or_404
from .models import EventUser
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
@login_required
@never_cache
def refere_view(request):
    eventUser = EventUser.objects.filter(status=0)
    
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        action = request.POST.get('action')
        
        event = get_object_or_404(EventUser, pk=event_id)
        
        if action == 'accept':
            event.accept_status = True
            event.reject_status = False
            
        elif action == 'reject':
            event.accept_status = False
            event.reject_status = True
        event.org_user=request.user
        event.save()
    
    return render(request, 'refere.html', {"eventUser": eventUser})

def view_history(request):
    orgs=request.user

    eventUser=EventUser.objects.filter(org_user=orgs,accept_status=True)
    # Assuming you have a queryset named eventUser that contains the event data
    # eventUser = EventUser.objects.all()  # You may need to adjust this query as per your models
    context = {
        'eventUser': eventUser
    }
    return render(request, 'Refere/view_history.html', context)

#**************************************************************ADMIN PANEL VIEWS.py**************************************************************
#admin panel        
def indexadmin(request):
     return render(request,'admin/indexadmin.html')


def dashboard(request):
    # Retrieve the count of users
    user_count = CustomUser.objects.count()

    return render(request, 'dashboard.html', {'user_count': user_count})

from django.shortcuts import render
from .models import CustomUser  # Import your NewUser model or the appropriate model for new users

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import EventUser

def edit_event(request, event_id):
    # Get the event instance by its ID
    event = get_object_or_404(EventUser, pk=event_id)

    if request.method == 'POST':
        # Update event fields based on POST data
        event.name = request.POST.get('name')
        event.description = request.POST.get('description')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time')
        event.location = request.POST.get('location')
        event.max_registrations = request.POST.get('max_registrations')
        event.close_event_date = request.POST.get('close_event_date')

        # Handle the event image upload if needed
        if 'image' in request.FILES:
            event.image = request.FILES['image']

        try:
            event.save()
        except Exception as e:
            return HttpResponseBadRequest("Error saving event data: {}".format(str(e)))

        # Redirect to the event details page or any other appropriate URL
        return redirect('Eventlist')
    elif request.method == 'GET':
        # If it's a GET request, render the edit form with the existing event details
        return render(request, 'admin/edit_Eventlist.html', {'event': event})
    else:
        return HttpResponseBadRequest("Invalid request method")

from django.shortcuts import render
from .models import CustomUser  # Import your CustomUser model

def new_user(request, user_type=None):
    # Determine the user type based on the URL parameter 'user_type'
    if user_type == 'customer':
        new_users = CustomUser.objects.filter(is_customer=True)
    elif user_type == 'refere':
        new_users = CustomUser.objects.filter(is_refere=True)
    else:
        # If 'user_type' is not provided or invalid, show all new users
        new_users = CustomUser.objects.all()

    # Pass the new_users data to the template
    context = {
        'new_users': new_users,
        'user_type': user_type,  # Pass user_type to the template to distinguish between customers and referees
    }

    # Render the template with the context data
    return render(request, 'admin/new_user.html', context)

#this is code for event registred deleteion
def delete_registration(request, pk):
    # Get the registration object or return a 404 error if it doesn't exist
    registration = get_object_or_404(Registration, pk=pk)

    if request.method == 'POST':
        # Perform the deletion
        registration.delete()

        # Add a success message (optional)
        messages.success(request, 'Registration deleted successfully.')

        # Redirect to a page after successful deletion
        return redirect('event_reg_player')  # Change this to your desired URL name

    # Handle GET request or other methods here
    return redirect('event_reg_player')  # Change this to your desired URL name

def event_reg_player(request):
    # Retrieve all registrations from the database
    registrations = Registration.objects.all()

    # Render the template with the registrations data
    return render(request, 'admin/event_reg_player.html', {'registrations': registrations})


def member(request):
    subscription_plans = SubscriptionPlan.objects.all()
     # Split the features field of each plan by line breaks
    for plan in subscription_plans:
        plan.features = plan.features.split('\n')
    return render(request, 'admin/member.html', {'subscription_plans': subscription_plans})

from django.shortcuts import render
from membershipapp.models import Payment_mem  # Import the Payment_mem model

def member_history(request):
    # Query the Payment_mem model to get a list of payment instances
    payments = Payment_mem.objects.all()

    # Create a dictionary to pass data to the template
    context = {
        'payments': payments,
    }

    return render(request, 'admin/member_history.html', context=context)



from django.http import JsonResponse

from django.http import JsonResponse

def deactivate_member(request, payment_id):
    try:
        payment = Payment_mem.objects.get(id=payment_id)
        # Update the 'status' field to '0' in your Payment_mem model
        payment.status = '0'
        payment.save()
        # Return a success response
        return JsonResponse({'status': 'success'})
    except Payment_mem.DoesNotExist:
        # Return an error response if the payment ID does not exist
        return JsonResponse({'status': 'error', 'message': 'Payment ID does not exist'})
def activate_member(request, payment_id):
    try:
        payment = Payment_mem.objects.get(id=payment_id)
        # Update the 'status' field to '1' to activate the member
        payment.status = '1'
        payment.save()
        # Redirect back to the member history page
        return JsonResponse({'status': 'success'})
    except Payment_mem.DoesNotExist:
        # Handle the case where the payment ID does not exist
        return JsonResponse({'status': 'error', 'message': 'Payment not found'})


def edit_member(request, plan_id):
    plan = get_object_or_404(SubscriptionPlan, pk=plan_id)

    if request.method == 'POST':
        # Get the updated data from the POST request
        title = request.POST.get('title')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        features = request.POST.get('features')

        # Update the plan object with the new data
        plan.title = title
        plan.price = price
        plan.duration = duration
        plan.features = features
        plan.save()

        return redirect('member')  # Redirect to a success page after saving

    return render(request, 'admin/edit_member.html', {'plan': plan})


def delete_subscription_plan(request, plan_id):
    plan = get_object_or_404(SubscriptionPlan, pk=plan_id)

    if request.method == 'POST':
        # Handle the deletion logic when the user confirms deletion
        plan.delete()
        return redirect('member')  # Redirect to the membership view after deletion

    return redirect('member')



# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import EventUser
from datetime import datetime

def add_event(request):
    if request.method == 'POST':
        try:
            # Get data from the POST request
            name = request.POST['name']
            description = request.POST['description']
            date = request.POST['date']
            time = request.POST['time']
            location = request.POST['location']
            image = request.FILES.get('image')
            close_event_date = request.POST.get('close_event_date')
            max_registrations = request.POST['max_registrations']

            # Initialize current_registrations
            current_registrations = request.POST.get('current_registrations', None)

            # Create a new EventUser object and save it to the database
            event = EventUser(
                name=name,
                description=description,
                date=date,
                time=time,
                location=location,
                image=image,
                close_event_date=close_event_date,
                max_registrations=max_registrations,
                current_registrations=current_registrations
            )
            event.save()

            # Redirect to the event list page or another page as needed
            return redirect('Eventlist')

        except Exception as e:
            return HttpResponseBadRequest("Error saving event data: {}".format(str(e)))

    return render(request, 'admin/add_event.html')  # Replace 'add_event.html' with your template path


def Eventlist(request):
    events_with_images = EventUser.objects.exclude(image__isnull=True)

    context = {
        'events': events_with_images,
    }

    events = EventUser.objects.all()
    return render(request, 'admin/Eventlist.html', {'events': events})

from django.shortcuts import render, get_object_or_404, redirect
from .models import EventUser

# 

def delete_event(request, event_id):
    try:
        event = EventUser.objects.get(pk=event_id)
        event.delete()
    except EventUser.DoesNotExist:
        # Handle the case where the event with the given ID doesn't exist
        pass
    return redirect('Eventlist') 


def add_winner(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        prize = request.POST.get('prize')
        image = request.FILES.get('image')
        print(image)

        # Create a Winner object and save it to the database
        Winner.objects.create(title=title, name=name, prize=prize, image=image)

        return redirect('winner_Gallery')  

    return render(request, 'admin/add_winner.html')


def add_member(request):
    if request.method == 'POST':
        # Get data from the POST request
        title = request.POST['title']
        price = request.POST['price']
        duration = request.POST['duration']
        features = request.POST['features']

        # Create a new SubscriptionPlan object and save it
        plan = SubscriptionPlan(title=title, price=price, duration=duration, features=features)
        plan.save()

        # Redirect to the membership page or any other page you want
        return redirect('member')
    else:
        return render(request, 'admin/add_member.html')




def winner_Gallery(request):
    # Fetch all winners from the database
    winners = Winner.objects.all()

    # Pass the winners to the template for rendering
    return render(request, 'admin/winner_Gallery.html', {'winners': winners})


def delete_winner(request, winner_id):
    winner = get_object_or_404(Winner, pk=winner_id)

    if request.method == 'POST':
        # Handle the deletion logic when the user confirms deletion
        winner.delete()
        return redirect('winner_Gallery')  # Redirect to the winners page after deletion

    return redirect('winner_Gallery')  # Redirect back to the winners page if not a POST request

def indexadmin(request):
    # Calculate the date threshold for "new" users (e.g., users created within the last 7 days)
    threshold_date = datetime.now() - timedelta(days=7)

    # Query new users from the database
    new_users = CustomUser.objects.filter(date_joined__gte=threshold_date)

    return render(request, 'admin/indexadmin.html', {'new_users': new_users})


  # this is guest booking player list in admin panel

def guestbook_player(request):
    # Fetch all booking records from the database
    bookings = Booking.objects.all()

    # Render the template with the bookings data
    return render(request, 'admin/guestbook_player.html', {'bookings': bookings})

# views.py guestbooking  page delete acton


def delete_booking(request, booking_id):
    # Get the Booking object to delete
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        # Handle the POST request (Delete confirmation)
        booking.delete()
        return redirect('guestbook_player') 
    return render(request, 'delete_booking_confirm.html', {'booking': booking})


#**************************************************************************************************************************
def Gallery(request):
    # Query the database to get all Winner objects
    winners = Winner.objects.all()
    # Render the gallery page template and pass the winners data to it
    return render(request, 'Gallery.html', {'winners': winners})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Winner

def edit_winner(request, winner_id):
    winner = get_object_or_404(Winner, id=winner_id)

    if request.method == 'POST':
        title = request.POST['title']
        name = request.POST['name']
        prize = request.POST['prize']
        image = request.FILES.get('image', winner.image)

        winner.title = title
        winner.name = name
        winner.prize = prize
        winner.image = image
        winner.save()

        return redirect('winner_Gallery')  # Redirect to the gallery page or any other desired page

    return render(request, 'admin/edit_Winner.html', {'winner': winner})

def EventRegform(request, event_id):
     event = get_object_or_404(EventUser, id=event_id)
     if request.method == 'POST':
          registration_type = request.POST.get('registration-type')

          # Check if registration_type is not empty
          if not registration_type:
               messages.error(request, 'Registration type is required.')
               return redirect('EventRegform', event_id=event_id)

          # Check if maximum registrations limit is reached
          current_registrations = event.current_registrations or 0  # Default to 0 if current_registrations is None
          if current_registrations >= event.max_registrations:
               messages.error(request, 'Booking is closed. Maximum registrations reached.')
               return redirect('EventRegform', event_id=event_id)

          event.current_registrations = current_registrations + 1
          event.save()

          name1 = request.POST.get('single-name') if registration_type == 'single' else request.POST.get('team-name1')
          dob1 = request.POST.get('single-dob') if registration_type == 'single' else request.POST.get('team-dob1')
          name2 = request.POST.get('team-name2') if registration_type == 'team' else None
          dob2 = request.POST.get('team-dob2') if registration_type == 'team' else None
          contact_number = request.POST.get('contact-number')
          declaration_accepted = 'declaration-checkbox' in request.POST
          print(registration_type)

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












# from .models import Profile_Verification
# from django.shortcuts import render, redirect
# from django.http import HttpResponse

# def ProfileVerification(request):
#     if request.method == 'POST':
#         destination_name = request.POST.get('destination_name')
#         category = request.POST.get('category')
#         destination_image = request.FILES['destination_image']

#         new_destination = Profile_Verification(
#             name=destination_name,
#             category=category,
#             image=destination_image,
#         )
#         new_destination.save()
#         return redirect('RegistrationSucess')  # Redirect to a success page URL

#     return render(request, 'ProfileVerification.html')  # Render the 'ProfileVerification.html' template



from django.shortcuts import render, redirect
from .models import Booking
from datetime import datetime, timedelta  # Import datetime


def get_booking_count_for_time_slot(booking_date, start_time, end_time):
    return Booking.objects.filter(
        booking_date=booking_date,
        booking_start_time__lte=start_time,
        booking_end_time__gte=end_time,
    ).count()

# views.py

from django.shortcuts import redirect, render
from django.urls import reverse

def Guestbooking(request):
    if request.method == "POST":
        client_name = request.POST.get("client-name")
        client_email = request.POST.get("client-email")
        client_phone = request.POST.get("client-phone")
        booking_date = request.POST.get("booking-date")
        booking_time = request.POST.get("booking-time")

        if client_name and client_email and booking_date and booking_time:
            # Split the time range into start and end times
            start_time, end_time = booking_time.split(" - ")

            # Create a datetime object for the booking date
            booking_datetime = datetime.strptime(booking_date, '%d %B %Y')

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

            # Calculate the booking count for the selected time slot
            booking_count = get_booking_count_for_time_slot(
                booking_datetime.date(), booking_datetime.time(), end_datetime.time()
            )

            # Check if the time slot is available
            if booking_count < 4:
                # Save the booking to the database
                Booking.objects.create(
                    client_name=client_name,
                    client_email=client_email,
                    client_phone=client_phone,
                    booking_date=booking_datetime.date(),
                    booking_start_time=booking_datetime.time(),
                    booking_end_time=end_datetime.time(),
                )

                # Redirect to the 'Guestpayment' view with query parameters
                redirect_url = reverse('Guestpayment')
                redirect_url += f'?client_name={client_name}&booking_count={booking_count + 1}'
                return redirect('Guestpayment')

            else:
                return render(
                    request,
                    "Guestbooking.html",
                    context={'error_message': 'This time slot is already fully booked.'}
                )

    return render(
        request,
        "Guestbooking.html",
    )




from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def Guestpayment(request):
    
	currency = 'INR'
	amount = 10000 # Rs. 200

	# Create a Razorpay Order
	razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
	razorpay_order_id = razorpay_order['id']
	callback_url = '/paymenthandler/'

	# we need to pass these details to frontend.
	context = {}
	context['razorpay_order_id'] = razorpay_order_id
	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
	context['razorpay_amount'] = amount
	context['currency'] = currency
	context['callback_url'] = callback_url

	return render(request, 'Payment.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

	# only accept POST request.
	if request.method == "POST":
		try:
		
			# get the required parameters from post request.
			payment_id = request.POST.get('razorpay_payment_id', '')
			razorpay_order_id = request.POST.get('razorpay_order_id', '')
			signature = request.POST.get('razorpay_signature', '')
			params_dict = {
				'razorpay_order_id': razorpay_order_id,
				'razorpay_payment_id': payment_id,
				'razorpay_signature': signature
			}

			# verify the payment signature.
			result = razorpay_client.utility.verify_payment_signature(
				params_dict)
			if result is not None:
				amount = 50000 # Rs. 200
				try:

					# capture the payemt
					razorpay_client.payment.capture(payment_id, amount)
                    
					# render success page on successful caputre of payment
					return redirect('/')

				except:

					# if there is an error while capturing payment.
					return render(request, 'paymentfail.html')
			else:

				# if signature verification fails.
				return render(request, 'paymentfail.html')
		except:

			# if we don't find the required parameters in POST data
			return HttpResponseBadRequest()
	else:
	# if other than POST request is made.
		return HttpResponseBadRequest()
# from django.shortcuts import render
# import razorpay
# from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseBadRequest


# # authorize razorpay client with API Keys.
# razorpay_client = razorpay.Client(
# 	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# # views.py

# def Guestpayment(request):
#     currency = 'INR'
#     amount = 10000  # Rs. 100

#     # Get query parameters
#     client_name = request.GET.get('client_name', '')
#     booking_count = request.GET.get('booking_count', '')

#     # Create a Razorpay Order
#     razorpay_order = razorpay_client.order.create(dict(amount=amount,
#                                                       currency=currency,
#                                                       payment_capture='0'))

#     # order id of newly created order.
#     razorpay_order_id = razorpay_order['id']
#     callback_url = 'paymenthandler/'

#     # we need to pass these details to frontend.
#     context = {}
#     context['razorpay_order_id'] = razorpay_order_id
#     context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
#     context['razorpay_amount'] = amount
#     context['currency'] = currency
#     context['callback_url'] = callback_url

#     return render(request, 'Payment.html', context=context)



# # we need to csrf_exempt this url as
# # POST request will be made by Razorpay
# # and it won't have the csrf token.
# @csrf_exempt
# def paymenthandler(request):
#     # Only accept POST request.
#     if request.method == "POST":
#             # Get the required parameters from the POST request.
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')
#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }

#             # Verify the payment signature.
#             result = razorpay_client.utility.verify_payment_signature(params_dict)
#             if result is not None:
#                     # Get the Payment_mem instance associated with the payment
#                     payment_instance = Payment_mem.objects.get(razorpay_order_id=razorpay_order_id)

                  
#                     razorpay_client.payment.capture(payment_id)

                    
                    
#                     return redirect('index')
