from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Player(AbstractUser):
    # Reputation score field
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    reputation_score = models.IntegerField(default=0, verbose_name='Puntuación de Reputación')
