from django.db.models.signals import post_delete, pre_save
from django.dispatch.dispatcher import receiver

from .models import Film

@receiver(post_delete, sender=Film)
def film_post_delete(sender, instance, **kwargs):
    if instance.poster:
        instance.poster.delete(False)

@receiver(pre_save, sender=Film)
def film_pre_save(sender, instance, **kwargs):
  if instance.pk:
    try:
      old_poster = sender.objects.get(pk=instance.pk).poster
      if old_poster != instance.poster:
        old_poster.delete(False) 
    except Film.DoesNotExist:
      pass
