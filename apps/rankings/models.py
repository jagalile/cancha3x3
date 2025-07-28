from django.db import models

# Create your models here.
class PlayerRanking(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    player = models.ForeignKey('users.Player', on_delete=models.CASCADE)
    elo = models.IntegerField(default=1500)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.player.username} - {self.elo} ELO"