from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("ranking_elo/", views.ranking_elo, name="ranking_elo"),
]
