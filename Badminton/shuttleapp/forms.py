# from django import forms
from .models import Booking

# class BookingForm1(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['date']
#         labels={'date':'DATE'}
#         widgets={
#             'date':forms.DateInput(attrs={'class':'datepicker'})
#         }

# class BookingForm2(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['time_slot']

# class BookingForm3(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['client_name', 'client_email', 'client_phone']
from django import forms


from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.TextInput(attrs={'class': 'datepicker'}),
        }