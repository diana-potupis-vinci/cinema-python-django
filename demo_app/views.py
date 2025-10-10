from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Film, Seance, Reservation
from .forms import ReservationForm, FilmForm


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

        return render(request, 'film/film-list.html', {"page_obj": page_obj})


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

        return render(request, 'film/film-details.html', context)
    
class SeanceView(View):
    def get(self, request):
        seances = Seance.objects.all()

        paginator = Paginator(seances, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'seances.html',  {"page_obj": page_obj})
    
def AboutView(request):
        return render(request, 'about.html')

class FilmCreateView(PermissionRequiredMixin, View):
    permission_required = 'demo_app.add_film'
    
    def get(self, request):
        form = FilmForm()
        return render(request, 'film/film_form.html', {'form': form})

    def post(self, request):
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save()
            messages.success(request, _('Le film a été ajouté avec succès!'))
            return redirect('film_detail', id=film.id)
        return render(request, 'film/film_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ReservationListView(View):
    def get(self, request):
        # cinema_admin et les employés peuvent voir toutes les réservations, les autres seulement les leurs
        if request.user.groups.filter(name='cinema_admin').exists() or request.user.groups.filter(name='employee').exists():
            reservations = Reservation.objects.all()
        else:
            reservations = Reservation.objects.filter(user=request.user)

        # Vérifions si l'utilisateur peut supprimer des réservations
        user_groups = request.user.groups.values_list('name', flat=True)
        can_delete_reservations = 'cinema_admin' in user_groups or 'employee' in user_groups

        paginator = Paginator(reservations, 10)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'can_delete_reservations': can_delete_reservations
        }

        return render(request, 'reservation/reservation_list.html', context)

@method_decorator(login_required, name='dispatch')
class ReservationCreateView(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'reservation/reservation_form.html', {'form': form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, _('Votre réservation a été créée avec succès!'))
            return redirect('reservation_list')
        return render(request, 'reservation/reservation_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ReservationUpdateView(View):
    def get(self, request, id):
        # cinema_admin peut modifier n'importe quelle réservation, les autres seulement les leurs
        if request.user.groups.filter(name='cinema_admin').exists():
            reservation = get_object_or_404(Reservation, id=id)
        else:
            reservation = get_object_or_404(Reservation, id=id, user=request.user)
        
        form = ReservationForm(instance=reservation)
        return render(request, 'reservation/reservation_form.html', {'form': form})

    def post(self, request, id):
        # cinema_admin peut modifier n'importe quelle réservation, les autres seulement les leurs
        if request.user.groups.filter(name='cinema_admin').exists():
            reservation = get_object_or_404(Reservation, id=id)
        else:
            reservation = get_object_or_404(Reservation, id=id, user=request.user)
            
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
        return render(request, 'reservation/reservation_form.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ReservationDeleteView(View):
    def post(self, request, id):
        # Vérifions si l'utilisateur a le droit de supprimer
        user_groups = request.user.groups.values_list('name', flat=True)
        
        if 'cinema_admin' in user_groups:
            # cinema_admin peut supprimer n'importe quelle réservation
            reservation = get_object_or_404(Reservation, id=id)
        elif 'employee' in user_groups:
            # employee peut supprimer n'importe quelle réservation
            reservation = get_object_or_404(Reservation, id=id)
        else:
            # Les clients ordinaires NE peuvent pas supprimer de réservations
            messages.error(request, _('Vous n\'avez pas la permission de supprimer cette réservation.'))
            return redirect('reservation_list')
            
        reservation.delete()
        messages.success(request, _('Votre réservation a été supprimée avec succès!'))
        return redirect('reservation_list')