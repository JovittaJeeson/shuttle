from django.contrib.auth import authenticate,login as auth_login
from django.shortcuts import redirect, render

from loginapp.models import CustomUser
from django.contrib import messages
# Create your views here.


def refere(request):
     return render(request,'refere.html')
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
                user.set_password(password)
                user.save() 
                messages.success(request, "Registered Successfully") 
                return redirect('login') 
    return render(request, 'Refere/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)                
                return redirect('/')  
            else:
                error_message = "Invalid login credentials."
                return render(request, 'login.html', {'error_message': error_message})
    return render(request,'Refere/login.html')