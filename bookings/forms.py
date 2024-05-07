# bookings/forms.py

from django import forms
from .models import Flight
from .models import Ticket


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['date', 'duration', 'price', 'available_seats', 'airline', 'origin', 'destination']

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['flight', 'passenger', 'seat_number']