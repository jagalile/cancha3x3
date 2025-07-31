from django.db.models.signals import post_delete
from django.dispatch import receiver
from apps.teams.models import Team


@receiver(post_delete, sender=Team)
def delete_logo_file(sender, instance, **kwargs):
    if instance.logo and instance.logo.path:
        instance.logo.delete(save=False)