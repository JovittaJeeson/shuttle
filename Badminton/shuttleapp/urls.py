from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
     path('',views.index,name='index'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     # path('membership/',views.membership,name='membership'),
     path('event_index/',views.event_index,name='event_index'),
     path('payment/',views.payment,name='payment'),
     path('Event_On_Trend/',views.Event_On_Trend,name='Event_On_Trend'),
     
     path('add_event/',views.add_event,name='add_event'),
     # path('EventRegform/<int:event_id>', views.EventRegform,name='EventRegform'),
     path('EventRegform/<int:event_id>/', views.EventRegform, name='EventRegform'),  # Define the URL pattern
     path('Guestbooking/',views.Guestbooking,name='Guestbooking'),
     path('RegistrationSucess/',views.RegistrationSucess,name='RegistrationSucess'),
     path('ProfileVerification/',views.ProfileVerification,name='ProfileVerification'),
     path('refere/',views.refere,name='refere'),
     path('Gallery/',views.Gallery,name='Gallery'),
     # path('Guestbooking/<int:timeslot_id>/', views.Guestbooking, name='Guestbooking'),
     # path('ticket/', views.download_ticket, name='download_ticket'),
     


     path('indexadmin/',views.indexadmin,name='indexadmin'),
     path('patients/',views.patients,name='patients'),
     path('doctors/',views.doctors,name='doctors')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
