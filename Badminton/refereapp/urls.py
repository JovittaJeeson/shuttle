from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
      # path('refere/',views.refere,name='refere'),
      path('register/',views.register,name='register'),
      path('Referelogin/',views.Referelogin,name='Referelogin'),
      path('trainer_register/', views.trainer_register, name='trainer_register'),
      # path('refere/<int:event_id>/', views.refere, name='refere'),
      path('user_logout/',views.user_logout,name='user_logout'),
]
