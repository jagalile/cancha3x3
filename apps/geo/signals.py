# users/signals.py
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import City, Court

@receiver(post_delete, sender=City)
def delete_logo_file(sender, instance, **kwargs):
    if instance.logo and instance.logo.path:
        instance.logo.delete(save=False)


@receiver(post_delete, sender=Court)
def delete_image_file(sender, instance, **kwargs):
    if instance.image and instance.image.path:
        instance.image.delete(save=False)
