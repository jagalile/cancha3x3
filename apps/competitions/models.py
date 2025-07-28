from django.db import models

# Create your models here.
class Competition(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Liga')
    description = models.TextField(blank=True, verbose_name='Descripción')
    city = models.ForeignKey('geo.City', on_delete=models.CASCADE, related_name='leagues', verbose_name='Ciudad')
    competition_type = models.CharField(max_length=50, choices=[
        ('league', 'Liga'),
        ('tournament', 'Torneo'),
    ], default='league', verbose_name='Tipo de Competencia')
    is_official = models.BooleanField(default=False, verbose_name='Es Oficial')
    start_date = models.DateField(verbose_name='Fecha de Inicio')
    end_date = models.DateField(verbose_name='Fecha de Fin')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competiciones'


class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name='matches', verbose_name='Competencia')
    round = models.CharField(max_length=50, verbose_name='Ronda')
    date = models.DateTimeField(verbose_name='Fecha y Hora')
    court = models.ForeignKey('geo.Court', on_delete=models.CASCADE, related_name='matches', verbose_name='Cancha')
    winner_team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, related_name='won_matches', verbose_name='Equipo Ganador')
    score_winner_team = models.IntegerField(default=0, verbose_name='Puntuación Equipo Ganador')
    loser_team = models.ForeignKey('teams.Team', on_delete=models.SET_NULL, null=True, related_name='lost_matches', verbose_name='Equipo Perdedor')
    score_loser_team = models.IntegerField(default=0, verbose_name='Puntuación Equipo Perdedor')
    is_verified = models.BooleanField(default=False, verbose_name='Está Verificado')

    def __str__(self):
        return f"{self.winner_team.name} vs {self.loser_team.name} - {self.date}"

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'