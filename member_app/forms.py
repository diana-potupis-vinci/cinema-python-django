from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and placeholders
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Choisissez un nom d\'utilisateur')
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Votre prénom')
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Votre nom de famille')
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('votre.email@example.com')
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Mot de passe sécurisé')
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Confirmez votre mot de passe')
        })
        
        # Update labels in French
        self.fields['password1'].label = _('Mot de passe')
        self.fields['password2'].label = _('Confirmer le mot de passe')
        self.fields['email'].label = _('Adresse email')
        self.fields['first_name'].label = _('Prénom')
        self.fields['last_name'].label = _('Nom')
        self.fields['username'].label = _('Nom d\'utilisateur')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes and placeholders
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Choisissez un nom d\'utilisateur')
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Votre prénom')
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('Votre nom de famille')
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': _('votre.email@example.com')
        })

        # Update labels in French
        self.fields['email'].label = _('Adresse email')
        self.fields['first_name'].label = _('Prénom')
        self.fields['last_name'].label = _('Nom')
        self.fields['username'].label = _('Nom d\'utilisateur')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
    
class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Ancien mot de passe')
        }),
        label=_('Ancien mot de passe')
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Nouveau mot de passe')
        }),
        label=_('Nouveau mot de passe'),
        min_length=8,
        help_text=_('Le mot de passe doit contenir au moins 8 caractères.')
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Confirmez le nouveau mot de passe')
        }),
        label=_('Confirmez le nouveau mot de passe')
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                self.add_error('new_password2', "Les nouveaux mots de passe ne correspondent pas.")
            elif len(new_password1) < 8:
                self.add_error('new_password1', "Le mot de passe doit contenir au moins 8 caractères.")
        
        return cleaned_data
    