from django.db import models

# Create your models here.
# store/models.py
from django.db import models
from django.urls import reverse

class Product(models.Model):
    printful_id = models.PositiveIntegerField(unique=True, help_text="El ID del producto en Printful")
    external_id = models.CharField(max_length=255, unique=True, help_text="El ID externo del producto en Printful")
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    thumbnail_url = models.URLField(max_length=1024)
    # Campos para almacenar maquetas pre-generadas
    mockup_front_url = models.URLField(max_length=1024, blank=True, null=True)
    mockup_back_url = models.URLField(max_length=1024, blank=True, null=True)
    # Otros campos que se puedan necesitar
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', kwargs={'slug': self.slug})