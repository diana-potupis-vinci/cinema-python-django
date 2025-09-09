from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('film/list/', views.FilmsListView.as_view(), name="film-list"),
    path('film/<int:id>/', views.FilmView.as_view(), name="film"),
]
