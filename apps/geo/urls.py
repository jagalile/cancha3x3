from django.urls import path

from . import views

app_name = "info"

urlpatterns = [
    path("cities/", views.cities, name="cities"),
    path("courts/", views.courts, name="courts"),
]
