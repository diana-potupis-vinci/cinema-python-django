from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Genre")

    def __str__(self):
        return self.name

class Film(models.Model):
  title = models.CharField(max_length=100, verbose_name="Titre")
  description = models.TextField(verbose_name="Description")
  duration = models.DurationField(verbose_name="Durée")
  genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name="Genre")
  poster = models.ImageField(verbose_name="Affiche", upload_to='img/', default='img/default.png')
  actors = models.ManyToManyField('Actor', related_name='films', verbose_name="Acteurs")

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title', )
    verbose_name = "film"
    verbose_name_plural = "films"

class Actor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Prénom")
    last_name = models.CharField(max_length=100, verbose_name="Nom")
    biography = models.TextField(max_length=300, verbose_name="Biographie")

    def __str__(self):
      return f"{self.last_name} {self.first_name}"

    class Meta:
      ordering = ('last_name', 'first_name' )
      verbose_name = "acteur"
      verbose_name_plural = "acteurs"

class Seance(models.Model):
   film = models.ForeignKey(Film, verbose_name="Films", related_name='seances', on_delete=models.CASCADE )
   date = models.DateField(verbose_name="Date")
   time = models.TimeField(verbose_name="Heure")
   hall = models.CharField(max_length=50, verbose_name="Salle")

   def __str__(self):
    return f"{self.film.title} - {self.date} à {self.time}"
   
   class Meta:
    ordering = ('date', 'time')
    verbose_name = "séance"
    verbose_name_plural = "séances"

class Reservation(models.Model):
   user = models.ForeignKey(User,verbose_name="Utilisateur", related_name='reservations', on_delete=models.CASCADE )
   seance = models.ForeignKey(Seance, verbose_name="Seance", related_name='reservations', on_delete=models.CASCADE)
   places = models.PositiveIntegerField(verbose_name="Places")
   reservation_date = models.DateTimeField(auto_now_add=True, verbose_name="Date réservation")

   def __str__(self):
      return f"{self.user.username} - {self.seance} ({self.places} places)"
   
   class Meta:
      ordering = ('reservation_date', )
      verbose_name = "réservation"
      verbose_name_plural = "réservations"