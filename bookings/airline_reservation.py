# airline_reservation/forms.py

from django import forms
from .models import Flight

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['date', 'duration', 'price', 'available_seats', 'airline', 'origin', 'destination']
