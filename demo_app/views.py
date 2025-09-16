from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import View

from .models import Film


class IndexView(View):
    def get(self, request):
        films = Film.objects.all()
        context = {
            'films': films,
        }
        return render(request, 'index.html', context)


class FilmsListView(View):
    def get(self, request):
        films = Film.objects.all()

        context = {
            'films': films,
        }

        return render(request, 'film-list.html', context)


class FilmView(View):
    def get(self, request, id):
        try:
            film = Film.objects.get(id=id)
        except Film.DoesNotExist:
            raise Http404("Film does not exist")
        

        context = {
            'film': film
        }

        return render(request, 'film-details.html', context)
