from django import forms
from .models import Reservation, Film, Genre, Actor

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

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'duration', 'genre', 'poster', 'actors']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'duration': 'Durée',
            'genre': 'Genre',
            'poster': 'Affiche',
            'actors': 'Acteurs',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM:SS'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
            'actors': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
        }