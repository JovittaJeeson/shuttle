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
                return redirect('Referelogin') 
    return render(request, 'Refere/register.html')

# def Referelogin(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('pass')

#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth_login(request, user)                
#                 return redirect('refere.html')  
#             else:
#                 error_message = "Invalid login credentials."
#                 return render(request, 'Refere/Referelogin.html', {'error_message': error_message})
#     return render(request,'Refere/Referelogin.html')
def Referelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('refere')
            else:
                messages.error(request, 'Invalid login credentials.')
                # Use messages.error to store the error message
                # This message will be available in the template

    return render(request, 'Refere/Referelogin.html')