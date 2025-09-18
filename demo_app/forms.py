from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['seance', 'places']
        labels = {
            'seance': 'Séance',
            'places': 'Nombre de places',
        }
        widgets = {
            'seance': forms.Select(attrs={'class': 'form-select'}),
            'places': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
