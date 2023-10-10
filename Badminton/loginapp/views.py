from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render
from .models import CustomUser
from datetime import datetime, timedelta

def jovilogin(request):
     return render(request,'jovilogin.html')

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
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
            user.is_customer=True
            user.set_password(password)
            user.save()
            messages.success(request,"registerd sucessfully")
            return redirect('login')
    return render(request, 'index_reg.html')

def jovilogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_refere:
                    return redirect("refere")
                elif user.is_customer:
                    return redirect('/')
                elif email == 'admin1@gmail.com':
                    return render(request, 'admin/indexadmin.html')
                else:
                    messages.error(request, 'Invalid login credentials.')
            else:
                messages.error(request, 'Invalid login credentials.')

    return render(request, 'jovilogin.html')











def user_logout(request):
    logout(request)
    return redirect('login')


#***************************************************************************************************************************************8



from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user  # Get the logged-in user

    if request.method == 'POST':
        # Update the user's profile details based on the POST data
        user.name = request.POST['name']
        user.birth = request.POST['birth']
        user.phone = request.POST['phone']
        user.gender = request.POST['gender']
        user.save()
        return redirect('user_profile')  # Redirect to the profile page after saving

    context = {
        'user': user,
    }
    return render(request, 'user_profile.html', context)
