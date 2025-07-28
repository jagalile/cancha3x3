from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Ciudad')
    province = models.CharField(max_length=100, verbose_name='Provincia')

    def __str__(self):
        return f"{self.name}, {self.province}"

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'


class Court(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Cancha')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='courts', verbose_name='Ciudad')
    address = models.CharField(max_length=255, verbose_name='Dirección')
    description = models.TextField(blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cancha'
        verbose_name_plural = 'Canchas'