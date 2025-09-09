from django.db import models

class Film(models.Model):
  title = models.CharField(max_length=100, verbose_name="Titre")
  description = models.TextField(verbose_name="Description")
  duration = models.DurationField(verbose_name="Durée")
  genre = models.CharField(max_length=100, verbose_name="Genre")

class Acteur(models.Model):
    name = models.CharField(max_length=100, verbose_name="Prénom")
    surname = models.CharField(max_length=100, verbose_name="Nom")
    biography = models.TextField(max_length=300, verbose_name="Biographie")
