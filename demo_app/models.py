from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Hall(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Salle"))

    def __str__(self):
        return self.name
    
    class Meta:
      ordering = ('name', )
      verbose_name = _("salle")
      verbose_name_plural = _("salles")

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_("Genre"))

    def __str__(self):
        return self.name
    
    class Meta:
      ordering = ('name', )
      verbose_name = _("genre")
      verbose_name_plural = _("genres")

class Film(models.Model):
  title = models.CharField(max_length=100, verbose_name=_("Titre"))
  description = models.TextField(verbose_name=_("Description"))
  duration = models.DurationField(verbose_name=_("Durée"))
  genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name=_("Genre"))
  poster = models.ImageField(verbose_name=_("Affiche"), upload_to='img/', default='img/default.png')
  actors = models.ManyToManyField('Actor', related_name='films', verbose_name=_("Acteurs"))

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title', )
    verbose_name = _("film")
    verbose_name_plural = _("films")

class Actor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("Prénom"))
    last_name = models.CharField(max_length=100, verbose_name=_("Nom"))
    biography = models.TextField(max_length=300, verbose_name=_("Biographie"))

    def __str__(self):
      return f"{self.last_name} {self.first_name}"

    class Meta:
      ordering = ('last_name', 'first_name' )
      verbose_name = _("acteur")
      verbose_name_plural = _("acteurs")

class Seance(models.Model):
   film = models.ForeignKey(Film, verbose_name=_("Films"), related_name='seances', on_delete=models.CASCADE )
   date = models.DateField(verbose_name=_("Date"))
   time = models.TimeField(verbose_name=_("Heure"))
   hall = models.ForeignKey(Hall, verbose_name=_("Salle"), related_name='seances', on_delete=models.CASCADE)

   def __str__(self):
    return f"{self.film.title} - {self.date} - {self.time}"
   
   class Meta:
    ordering = ('date', 'time')
    verbose_name = _("séance")
    verbose_name_plural = _("séances")

class Reservation(models.Model):
   user = models.ForeignKey(User,verbose_name=_("Utilisateur"), related_name='reservations', on_delete=models.CASCADE )
   seance = models.ForeignKey(Seance, verbose_name=_("Séance"), related_name='reservations', on_delete=models.CASCADE)
   places = models.PositiveIntegerField(verbose_name=_("Places"))
   reservation_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date réservation"))

   def __str__(self):
      return f"{self.user.username} - {self.seance} ({self.places} places)"
   
   class Meta:
      ordering = ('reservation_date', )
      verbose_name = _("réservation")
      verbose_name_plural = _("réservations")