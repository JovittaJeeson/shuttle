
from .models import Booking
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