from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('films/', views.FilmsListView.as_view(), name="film-list"),
    path('films/<int:id>/', views.FilmView.as_view(), name="film_detail"),
    path('films/add/', views.FilmCreateView.as_view(), name='film_add'),
    path('seances/', views.SeanceView.as_view(), name="seances"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', views.AboutView, name='about'),
    path('reservations/', views.ReservationListView.as_view(), name='reservation_list'),
    path('reservations/new/', views.ReservationCreateView.as_view(), name='reservation_create'),
    path('reservations/<int:id>/edit/', views.ReservationUpdateView.as_view(), name='reservation_edit'),
    path('reservations/<int:id>/delete/', views.ReservationDeleteView.as_view(), name='reservation_delete'),
]
