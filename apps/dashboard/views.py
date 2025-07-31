from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.rankings.models import PlayerRanking
from django.db.models import Max, Subquery, OuterRef, Avg, Q
from django.db.models.functions import TruncDate

from apps.teams.models import Team, TeamMember


# Create your views here.
@login_required
def dashboard(request):
    user = request.user
    return render(request, "dashboard.html", {"user": user})


@login_required
def ranking_elo(request):
    player_ranking = _get_ordered_player_ranking()

    team_ranking = _get_ordered_team_ranking()

    return render(
        request,
        "ranking_elo.html",
        {"player_ranking": player_ranking, "team_ranking": team_ranking},
    )


def _get_ordered_player_ranking():
    latest_ids = (
        PlayerRanking.objects.values("player_id")
        .annotate(latest_id=Max("id"))
        .values_list("latest_id", flat=True)
    )
    player_ranking = (
        PlayerRanking.objects.filter(id__in=latest_ids)
        .select_related("player")  # Carga todos los datos de Player
        .order_by("-elo", "player__username")
    )

    return player_ranking


def _get_ordered_team_ranking():
    today = date.today()

    # Subconsulta para obtener el último ELO por jugador
    latest_ranking_subquery = (
        PlayerRanking.objects.filter(player=OuterRef("player"))
        .order_by("-date")
        .values("elo")[:1]
    )

    # 1. Anotar fechas truncadas en TeamMember
    active_members = (
        TeamMember.objects.annotate(
            join_date_only=TruncDate("join_date"),
            leave_date_only=TruncDate("leave_date"),
        )
        .filter(
            Q(join_date_only__lte=today),
            Q(leave_date_only__isnull=True) | Q(leave_date_only__gte=today),
        )
        .annotate(latest_elo=Subquery(latest_ranking_subquery))
    )

    # 2. Anotar equipos con el promedio de ELO de sus miembros activos
    teams_with_avg_elo = Team.objects.filter(members__in=active_members).annotate(
        average_elo=Avg(
            Subquery(
                PlayerRanking.objects.filter(player=OuterRef("members__player"))
                .order_by("-date")
                .values("elo")[:1]
            )
        )
    )

    return teams_with_avg_elo
