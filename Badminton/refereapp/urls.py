from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
      path('refere/',views.refere,name='refere'),
      path('register/',views.register,name='register'),
      path('login/',views.register,name='login'),
]
