from django.urls import path

from . import views

app_name = "rankings"

urlpatterns = [
    path("ranking_elo_players/", views.ranking_elo_players, name="ranking_elo_players"),
    path("ranking_elo_teams/", views.ranking_elo_teams, name="ranking_elo_teams"),
]
