from django.contrib.auth import authenticate,login as auth_login
from django.shortcuts import redirect, render

from loginapp.models import CustomUser
from django.contrib import messages
# Create your views here.


def refere(request):
     return render(request,'refere.html')

def trainer_register(request): 
    if request.method=='POST': 
        name = request.POST.get('name')  
        email = request.POST.get('email') 
        password = request.POST.get('password')      
        if email and password: 
           
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request,"Email is already registered")
            else: 
                user = CustomUser(name=name,email=email) 
                user.is_trainer=True
                
                user.set_password(password)
                user.save() 
                messages.success(request, "Registered Successfully") 
                return redirect('login') 
    return render(request, 'Refere/trainer_register.html')

                
def register(request): 
    if request.method=='POST': 
        name = request.POST.get('name')  
        email = request.POST.get('email') 
        password = request.POST.get('password')      
        if email and password: 
           
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request,"Email is already registered")
            else: 
                user = CustomUser(name=name,email=email) 
                user.is_refere=True
                user.set_password(password)
                user.save() 
                messages.success(request, "Registered Successfully") 
                return redirect('login') 
    return render(request, 'Refere/register.html')




  
from django.contrib.auth import login
def Referelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None and user.is_refere:  # Check if the user is a referee
                login(request, user)
                return redirect('refere')
            else:
                messages.error(request, 'Invalid login credentials.')

    return render(request, 'Refere/Referelogin.html')

from django.contrib.auth import logout as auth_logout
def user_logout(request):
    auth_logout(request)
    return redirect('index')

from django.shortcuts import render, get_object_or_404, redirect
from shuttleapp.models import EventUser

from django.shortcuts import render, redirect

from django.contrib import messages

# from django.shortcuts import render
  # Import your Event model

# def refere_view(request):
#     # Fetch the events from your database
#     events = EventUser.objects.all()  # You can customize this queryset as needed

#     # You can perform any additional processing here if necessary

#     context = {
#         'eventUser': events  # Pass the events to your template
#     }

#     return render(request, 'refere.html', context)
