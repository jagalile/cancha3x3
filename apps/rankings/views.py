from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.rankings.models import PlayerRanking
from apps.teams.models import Team, TeamMember
from django.db.models.functions import TruncDate
from django.db.models import Avg, Subquery, OuterRef, Q, Max
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template.loader import render_to_string

ITEMS_PER_PAGE = 10

# Create your views here.
@login_required
def ranking_elo_players(request):
    page_number = request.GET.get("page", 1)
    player_ranking, start_index = _get_ordered_player_ranking(page_number)
    historical_player_ranking = _get_historical_players_ranking()
    user = request.user

    if request.htmx:
        html = render_to_string(
            "partials/partial_ranking_table.html",
            {
                "player_ranking": player_ranking,
                "historical_player_ranking": historical_player_ranking,
                "user": user,
                "start_index": start_index,
            },
        )
        return HttpResponse(html)

    return render(
        request,
        "elo_tables.html",
        {
            "player_ranking": player_ranking,
            "historical_player_ranking": historical_player_ranking,
            "user": user,
            "start_index": start_index,
        },
    )


@login_required
def ranking_elo_teams(request):
    page_number = request.GET.get("page", 1)
    team_ranking, start_index = _get_ordered_team_ranking(page_number)

    if request.htmx:
        html = render_to_string(
            "partials/partial_ranking_table.html",
            {
                "team_ranking": team_ranking,
                "start_index": start_index,
            },
        )
        return HttpResponse(html)

    return render(
        request,
        "elo_tables.html",
        {
            "team_ranking": team_ranking,
            "start_index": start_index,
        },
    )


def _get_ordered_player_ranking(page_number, per_page=ITEMS_PER_PAGE):
    latest_ids = (
        PlayerRanking.objects.values("player_id")
        .annotate(latest_id=Max("id"))
        .values_list("latest_id", flat=True)
    )
    player_ranking = (
        PlayerRanking.objects.filter(id__in=latest_ids)
        .select_related("player")
        .order_by("-elo", "player__username")
    )

    paginator = Paginator(player_ranking, per_page)
    players = paginator.get_page(page_number)

    return players, (int(page_number) - 1) * per_page


def _get_historical_players_ranking():
    best_rankings = PlayerRanking.objects.filter(player=OuterRef("player")).order_by(
        "-elo"
    )

    historical_players_ranking = (
        PlayerRanking.objects.select_related("player")
        .filter(pk=Subquery(best_rankings.values("pk")[:1]))
        .order_by("-elo", "player__username")
    )

    return historical_players_ranking


def _get_ordered_team_ranking(page_number, per_page=ITEMS_PER_PAGE):
    today = date.today()

    latest_ranking_subquery = (
        PlayerRanking.objects.filter(player=OuterRef("player"))
        .order_by("-date")
        .values("elo")[:1]
    )

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

    teams_with_avg_elo = (
        Team.objects.filter(members__in=active_members)
        .annotate(
            average_elo=Avg(
                Subquery(
                    PlayerRanking.objects.filter(player=OuterRef("members__player"))
                    .order_by("-date")
                    .values("elo")[:1]
                )
            )
        )
        .order_by("-average_elo", "name")
    )

    paginator = Paginator(teams_with_avg_elo, per_page)
    players = paginator.get_page(page_number)

    return players, (int(page_number) - 1) * per_page
