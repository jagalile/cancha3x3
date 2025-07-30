from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Equipo')
    is_active = models.BooleanField(default=True, verbose_name='Está Activo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', verbose_name='Equipo')
    player = models.ForeignKey('users.Player', on_delete=models.CASCADE, related_name='team_members', verbose_name='Usuario')
    join_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Unión')
    leave_date = models.DateTimeField(null=True, blank=True, verbose_name='Fecha de Salida')
    is_captain = models.BooleanField(default=False, verbose_name='Es Capitán')

    def __str__(self):
        return f"{self.player.username} - {self.team.name}"

    class Meta:
        verbose_name = 'Miembro del Equipo'
        verbose_name_plural = 'Miembros del Equipo'