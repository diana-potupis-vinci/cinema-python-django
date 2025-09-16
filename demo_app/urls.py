from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('films/', views.FilmsListView.as_view(), name="film-list"),
    path('films/<int:id>/', views.FilmView.as_view(), name="film_detail"),
    path('seances/', views.SeanceView.as_view(), name="seances"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
