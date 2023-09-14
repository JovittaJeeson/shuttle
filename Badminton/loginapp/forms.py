from django import forms
from .models import UserProfile


class Organizer(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
