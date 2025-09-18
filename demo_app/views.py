from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Film, Seance


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
