from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render
from .models import CustomUser
from datetime import datetime, timedelta



from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def user_profile(request):
     return render(request,'user_profile.html')
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import CustomUser

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import CustomUser

def jovilogin(request):
    # Initialize the context variable to False by default
    register_successful = False

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pwd')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_refere:
                    return redirect("refere")
                elif user.is_trainer:
                    return redirect("indextrainer")
                elif user.is_customer:
                    return redirect('/')
                elif email == 'admin1@gmail.com':
                    return render(request, 'admin/indexadmin.html')
            else:
                # Set an error message to be displayed in the template
                messages.error(request, 'Login Failed: Invalid email or password')

    # Check if the 'register_successful' key is in the request's GET parameters
    if 'register_successful' in request.GET:
        # Set the context variable to True if 'register_successful' is present
        register_successful = True

    return render(request, 'jovilogin.html', {'register_successful': register_successful})
from django.contrib import messages

def index_reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('fname')
        birth = request.POST.get('birth')
        password = request.POST.get('pwd')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'Email is already registered')
        elif email and name and birth and password and gender and phone:
            user = CustomUser(email=email, name=name, birth=birth, gender=gender, phone=phone)
            user.is_customer = True
            user.set_password(password)
            user.save()
            # Set a success message and clear it from the list of messages
            messages.get_messages(request)._loaded_data = []
            # messages.success(request, 'Registered Successfully')
            return redirect('login')

    return render(request, 'index_reg.html')



# def index_reg(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         name = request.POST.get('fname') 
#         birth = request.POST.get('birth')   
#         password = request.POST.get('pwd')  
#         gender = request.POST.get('gender')  
#         phone = request.POST.get('phone')    
        

#         if CustomUser.objects.filter(email=email).exists():
#             messages.info(request,'Email is already registered')
#             return render(request,"index_reg.html")
#         elif email and name and birth and password and gender and phone:
#             user = CustomUser(email=email,name=name,birth=birth,gender=gender,phone=phone)
#             user.is_customer=True
#             user.set_password(password)
#             user.save()
#             messages.success(request,"registerd sucessfully")
#             return redirect('login')
#     return render(request, 'index_reg.html')

# def jovilogin(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('pwd')

#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 if user.is_refere:
#                     return redirect("refere")
#                 elif user.is_customer:
#                     return redirect('/')
#                 elif email == 'admin1@gmail.com':
#                     return render(request, 'admin/indexadmin.html')
#                 else:
#                   error_message="invalid login credintials"
#                   return render(request, 'jovilogin.html',{'error_message': error_message})

#     messages.clear(request)
#     return render(request, 'jovilogin.html')






#***********************************
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login

# def jovilogin(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('pwd')

#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 if user.is_refere:
#                     return redirect("refere")
#                 elif user.is_customer:
#                     return redirect('/')
#                 elif email == 'admin1@gmail.com':
#                     return render(request, 'admin/indexadmin.html')
#             else:
#                 # Set an error message to be displayed in the template
#                 messages.error(request, 'Login Failed: Invalid email or password')

#     # For successful registration message
#     if 'register_successful' in request.GET:
#         messages.success(request, 'Registered Successfully')

#     return render(request, 'jovilogin.html')












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
