from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone_number', 'email', 'car_model', 'date', 'service']
        widgets = {
            'service': forms.Select(choices=Reservation.SERVICE_CHOICES),
        }


