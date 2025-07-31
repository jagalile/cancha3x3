from django.urls import path

from . import views

app_name = "rankings"

urlpatterns = [
    path("ranking_elo/", views.ranking_elo, name="ranking_elo"),
]
