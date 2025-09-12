from django.contrib import admin

from .models import Film, Genre, Actor, Seance, Reservation

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    search_fields = ('last_name', 'first_name')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'duration')
    list_filter = ('genre',)
    search_fields = ('title',)
    filter_horizontal = ('actors',)

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'date', 'time', 'hall')
    list_filter = ('film', 'hall', 'date', 'time')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'seance', 'places', 'reservation_date')
    list_filter = ('seance', 'user')