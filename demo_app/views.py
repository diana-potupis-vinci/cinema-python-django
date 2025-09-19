from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib import messages

from .models import Film, Seance, Reservation
from .forms import ReservationForm, UserRegistrationForm, FilmForm


class IndexView(View):
    def get(self, request):
        films = Film.objects.all()

        paginator = Paginator(films, 6)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    
        return render(request, 'index.html',  {"page_obj": page_obj})


class FilmsListView(View):
    def get(self, request):
        films = Film.objects.all()

        paginator = Paginator(films, 9)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'film-list.html', {"page_obj": page_obj})


class FilmView(View):
    def get(self, request, id):
        try:
            film = Film.objects.get(id=id)
        except Film.DoesNotExist:
            raise Http404("Film does not exist")
        
        today = timezone.localdate()

        seances = Seance.objects.filter(film=film, date__gte=today).order_by('date', 'time')

        context = {
            'film': film,
            'seances': seances,
        }

        return render(request, 'film-details.html', context)
    
class SeanceView(View):
    def get(self, request):
        seances = Seance.objects.all()

        context = {
            'seances': seances,
        }

        return render(request, 'seances.html', context)
    
def AboutView(request):
        return render(request, 'about.html')

@method_decorator(login_required, name='dispatch')
class FilmCreateView(View):
    def get(self, request):
        form = FilmForm()
        return render(request, 'film_form.html', {'form': form})

    def post(self, request):
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save()
            messages.success(request, 'Le film a été ajouté avec succès!')
            return redirect('film_detail', id=film.id)
        return render(request, 'film_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ReservationListView(View):
    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user)
        return render(request, 'reservation_list.html', {'reservations': reservations})


@method_decorator(login_required, name='dispatch')
class ReservationCreateView(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'reservation_form.html', {'form': form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Votre réservation a été créée avec succès!')
            return redirect('reservation_list')
        return render(request, 'reservation_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ReservationUpdateView(View):
    def get(self, request, id):
        reservation = get_object_or_404(Reservation, id=id, user=request.user)
        form = ReservationForm(instance=reservation)
        return render(request, 'reservation_form.html', {'form': form})

    def post(self, request, id):
        reservation = get_object_or_404(Reservation, id=id, user=request.user)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
        return render(request, 'reservation_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ReservationDeleteView(View):
    def post(self, request, id):
        reservation = get_object_or_404(Reservation, id=id, user=request.user)
        reservation.delete()
        return redirect('reservation_list')

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