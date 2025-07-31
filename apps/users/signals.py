from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Player

@receiver(post_delete, sender=Player)
def delete_avatar_file(sender, instance, **kwargs):
    if instance.avatar and instance.avatar.path:
        instance.avatar.delete(save=False)