from modeltranslation.translator import register, TranslationOptions
from .models import Hall, Genre, Film, Actor

@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Genre)
class GenreTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Film)
class FilmTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Actor)
class ActorTranslationOptions(TranslationOptions):
    fields = ('biography',)
