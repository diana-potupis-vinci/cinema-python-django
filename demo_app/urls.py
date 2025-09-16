from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('films/', views.FilmsListView.as_view(), name="film-list"),
    path('films/<int:id>/', views.FilmView.as_view(), name="film_detail"),
]
