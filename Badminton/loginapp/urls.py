from django.contrib import admin
from django.urls import path
from.import views
from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('login',views.jovilogin,name='login'),
    path('index_reg/',views.index_reg,name='index_reg'),
    path('logout/',views.user_logout,name='logout'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),     
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),     
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('user_profile/',views.user_profile,name='user_profile'),
    # path('user_profile/',views.user_profile,name='user_profile'),
  
]
