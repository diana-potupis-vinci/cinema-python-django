from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('films/', views.FilmsListView.as_view(), name="film-list"),
    path('films/<int:id>/', views.FilmView.as_view(), name="film_detail"),
    path('films/add/', views.FilmCreateView.as_view(), name='film_add'),
    path('films/<int:id>/delete/', views.FilmDeleteView.as_view(), name='film_delete'),
    path('seances/', views.SeanceView.as_view(), name="seances"),
    path('about/', views.AboutView, name='about'),
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservations/new/', views.ReservationCreateView.as_view(), name='reservation_create'),
    path('reservations/<int:id>/edit/', views.ReservationUpdateView.as_view(), name='reservation_edit'),
    path('reservations/<int:id>/delete/', views.ReservationDeleteView.as_view(), name='reservation_delete'),
]
