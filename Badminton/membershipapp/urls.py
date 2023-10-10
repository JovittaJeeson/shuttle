from django.contrib import admin
from django.urls import path
from.import views

urlpatterns=[
     path('membership/',views.membership,name='membership'),
     path('Payment/<int:member_id>',views.Payment,name='Payment'),
     path('paymenthandler/', views.paymenthandler, name='paymenthandler'), 
     path('create_payment/<int:subscription_plan_id>', views.create_payment, name='create_payment'), 
]
     