from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

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
    ordering = ('last_name', 'first_name')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_name_with_poster', 'genre', 'duration', 'view_actors_link')
    list_filter = ('genre',)
    search_fields = ('title', 'actors__first_name', 'actors__last_name')
    readonly_fields = ('poster_preview',)
    filter_horizontal = ('actors',)

    def film_name_with_poster(self, obj):
        if obj.poster:
            return format_html(
                '<span style="display:flex; align-items:center;">'
                '<img src="{}" style="max-width:50px; margin-right:6px;" />'
                '{}'
                '</span>',
                obj.poster.url,
                obj.title
            )
        return obj.title
    film_name_with_poster.short_description = 'Nom'
    film_name_with_poster.admin_order_field = 'title'

    def poster_preview(self, obj):
        if obj.poster:
            return format_html('<img src="{}" style="max-width:200px;"/>', obj.poster.url)
        return "No poster available"
    poster_preview.short_description = 'Poster Preview'

    def view_actors_link(self, obj):
        if not obj.pk:
            return "-"
        
        url = (
            reverse("admin:demo_app_actor_changelist")
            + f"?films__id__exact={obj.id}"
        )
        return format_html(
            '<a href="{}">Voir les acteurs</a>', 
            url, 
        )

    view_actors_link.short_description = "Acteurs"

@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    list_display = ('film', 'date', 'time', 'hall')
    list_filter = ('film', 'hall', 'date',)
    search_fields = ('film__title', 'hall__name')
    ordering = ('date', 'time')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'film_title', 'seance_date', 'places', 'reservation_date_only')

    def film_title(self, obj):
        return obj.seance.film.title
    film_title.short_description = 'Film'

    def seance_date(self, obj):
        return obj.seance.date
    seance_date.short_description = 'Seance Date'

    def reservation_date_only(self, obj):
        return obj.reservation_date.date()
    reservation_date_only.short_description = 'Reservation Date'
    list_filter = ('seance__film__title', 'seance__date', 'user')
    search_fields = ('user__username', 'seance__film__title')
    readonly_fields = ('reservation_date',)
    ordering = ('-reservation_date',)
