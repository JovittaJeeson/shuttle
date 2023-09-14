from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import CustomUser
# Create your views here.
from django.contrib import messages

def jovilogin(request):
     return render(request,'jovilogin.html')
def user_profile(request):
     return render(request,'user_profile.html')

def index_reg(request):
    if request.method=='POST':
        email = request.POST.get('email')
        name = request.POST.get('fname') 
        birth = request.POST.get('birth')   
        password = request.POST.get('pwd')  
        gender = request.POST.get('gender')  
        phone = request.POST.get('phone')    
        

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request,'Email is already registered')
            return render(request,"index_reg.html")
        elif email and name and birth and password and gender and phone:
            user = CustomUser(email=email,name=name,birth=birth,gender=gender,phone=phone)
            user.set_password(password)
            user.save()
            messages.success(request,"registerd sucessfully")
            return redirect('login')
    return render(request, 'index_reg.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout



from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages module
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages

def jovilogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid login credentials.')
                # Use messages.error to store the error message
                # This message will be available in the template

    return render(request, 'jovilogin.html')


# def jovilogin(request):

#     print("Entered")
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('pwd')

#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth_login(request, user)                
#                 return redirect('/')  
#             else:
#                 messages.info(request,'Invalid login credentials.')
#                 return render(request, 'jovilogin.html')
#         # else:
#         #     error_message = "Please fill out all fields."
#         #     return render(request, 'Login.html', {'error_message': error_message})

#     return render(request, 'jovilogin.html')




def user_logout(request):
    logout(request)
    return redirect('login')


#***************************************************************************************************************************************8


#userprofile

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile  # Import your UserProfile model
from .forms import Organizer
# @login_required
# def user_profile(request):
#     user_profile = UserProfile.objects.get(user=request.user)
@login_required
def user_profile(request):
    orgs=request.user
    try:
        task=UserProfile.objects.get(user=orgs)
    except UserProfile.DoesNotExist:
        if request.method == "POST":
            form = Organizer(request.POST)
            if form.is_valid():
                event_organizer = form.save(commit=False)
                event_organizer.user = orgs  # Set the user association
                event_organizer.save()
                return redirect('user_profile')
        else:
            form = Organizer()
    else:
        form=Organizer(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    return render(request, 'user_profile.html', {'form': form})

# @login_required
# def user_profile(request):
    
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
#     if request.method == "POST":
#         # Handle the form submission
#         user_profile.full_name = request.POST.get('full_name')
#         user_profile.email = request.POST.get('email')
#         user_profile.date_of_birth = request.POST.get('date_of_birth')
#         user_profile.phone_number = request.POST.get('phone_number')
#         user_profile.gender = request.POST.get('gender')
#         profile_picture = request.FILES.get('profile_picture')

#         # Check if a profile picture was uploaded and save it
#         if profile_picture:
#             user_profile.profile_picture = profile_picture

#         user_profile.save()
#         return redirect('user_profile')  # Redirect to the profile page after saving

#     return render(request, 'user_profile.html', {'user_profile': user_profile})

