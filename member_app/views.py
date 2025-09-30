from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.contrib.auth import login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from member_app.forms import PasswordChangeForm, UserRegistrationForm, UserChangeForm

# Create your views here.
class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Votre compte a été créé avec succès!')
            return redirect('login')
        return render(request, 'register.html', {'form': form})

class UserChangeView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Votre profil a été mis à jour avec succès!')
        return super().form_valid(form)

class PasswordChangeView(LoginRequiredMixin, View):
    def get(self, request):
        form = PasswordChangeForm()
        return render(request, 'password_change.html', {'form': form})
    
    def post(self, request):
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            user = request.user
            # Vérifier l'ancien mot de passe
            if not user.check_password(form.cleaned_data['old_password']):
                form.add_error('old_password', 'L\'ancien mot de passe est incorrect.')
                return render(request, 'password_change.html', {'form': form})
            
            # Changer le mot de passe
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            
            # Maintenir la session utilisateur après changement de mot de passe
            update_session_auth_hash(request, user)
            
            messages.success(request, 'Votre mot de passe a été changé avec succès!')
            return redirect('index')
        
        return render(request, 'password_change.html', {'form': form})
