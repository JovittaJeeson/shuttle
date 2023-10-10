from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
     path('',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     
     path('event_index/',views.event_index,name='event_index'),
     # path('payment/',views.payment,name='payment'),
     path('Event_On_Trend/',views.Event_On_Trend,name='Event_On_Trend'),
     
     
     path('EventRegform/<int:event_id>/', views.EventRegform, name='EventRegform'),  # Define the URL pattern
     path('Guestbooking/',views.Guestbooking,name='Guestbooking'),
     path('RegistrationSucess/',views.RegistrationSucess,name='RegistrationSucess'),
     # path('ProfileVerification/',views.ProfileVerification,name='ProfileVerification'),
     path('refere/',views.refere_view,name='refere'),
     path('Gallery/',views.Gallery,name='Gallery'),
     # path('Guestbooking/<int:timeslot_id>/', views.Guestbooking, name='Guestbooking'),
     # path('ticket/', views.download_ticket, name='download_ticket'),
     path('refere/', views.refere_view, name='refere'),
     path('view-history/', views.view_history, name='view_history'),
#admin panel path
     path('indexadmin/',views.indexadmin,name='indexadmin'),
     path('new_user/', views.new_user, name='new_user'), 
     path('member/',views.member,name='member'),
     path('add_member/',views.add_member,name='add_member'),
     path('member_history/', views.member_history, name='member_history'),
     path('deactivate_member/<int:payment_id>/', views.deactivate_member, name='deactivate_member'),
     path('activate_member/<int:payment_id>/', views.activate_member, name='activate_member'),


     path('new-user/', views.new_user, name='new_user'),  # For all new users
     path('new-user/customer/', views.new_user, {'user_type': 'customer'}, name='new_user_customer'),  # For customers
     path('new-user/referee/', views.new_user, {'user_type': 'referee'}, name='new_user_referee'),  # For referees

     # path('edit_member/',views.edit_member,name='edit_member'),
     path('edit_member/<int:plan_id>/', views.edit_member, name='edit_member'),
     path('delete_subscription_plan/<int:plan_id>/', views.delete_subscription_plan, name='delete_subscription_plan'),
     path('winner_Gallery/',views.winner_Gallery,name='winner_Gallery'),
     path('add_winner/',views.add_winner,name='add_winner'),
     path('edit_winner/<int:winner_id>/', views.edit_winner, name='edit_winner'),
     path('delete_winner/<int:winner_id>/', views.delete_winner, name='delete_winner'),

     # path('Eventlist/<int:event_id>/', views.Eventlist, name='Eventlist'),

     path('Eventlist/',views.Eventlist,name='Eventlist'),
     path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
     path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
     path('add_event/',views.add_event,name='add_event'),
     
     path('event_reg_player/', views.event_reg_player, name='event_reg_player'),
     path('delete_registration/<int:pk>/', views.delete_registration, name='delete_registration'),
     path('guestbook_player/', views.guestbook_player,name='guestbook_player'),
     # url of guestbooking page delete action
     path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),

#payment
     # path('Guestpayment/<str:client_name>/<int:booking_count>/', views.Guestpayment, name='Guestpayment'),
     path('Guestpayment/', views.Guestpayment, name='Guestpayment'),
     # path('Guestpayment/',views.Guestpayment,name='Guestpayment'),
     path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
