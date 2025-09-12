from django.contrib import admin

from .models import Film, Genre, Actor, Hall, Seance, Reservation

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    search_fields = ('last_name', 'first_name')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'duration')
    list_filter = ('genre',)
    search_fields = ('title',)
    filter_horizontal = ('actors',)

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = ('film', 'date', 'time', 'hall')
    list_filter = ('film', 'hall', 'date', 'time')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'seance', 'places', 'reservation_date')
    list_filter = ('seance', 'user')
