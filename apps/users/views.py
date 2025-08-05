from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from apps.rankings.models import PlayerRanking
from apps.teams.models import Team
from apps.competitions.models import Match
from apps.users.forms import CustomLoginForm, SignUpForm
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.db.models import Q
from django.db.models.functions import TruncDate
from apps.users.models import Player


# Create your views here.
class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy("dashboard:dashboard")


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard:dashboard")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        CustomLoginView(self.request, user)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        redirect_url = reverse_lazy("users:login")  # o cualquier otra ruta
        response = JsonResponse({}, status=200)
        response["HX-Redirect"] = redirect_url
        return response


class PublicProfileView(TemplateView):
    template_name = "public_profile.html"
    success_url = reverse_lazy("dashboard:dashboard")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        user = self.get_user(user_id)
        context["user"] = user
        context["total_games"] = _get_player_number_of_games(user)
        context["current_elo"] = _get_player_current_elo(user)
        context["highest_elo"] = _get_highest_elo(user)
        context["reputation"] = user.reputation_score
        context["current_teams"] = _get_player_current_teams(user)
        return context

    def get_user(self, user_id):
        try:
            return Player.objects.get(id=user_id)
        except Player.DoesNotExist:
            return None


def _get_player_number_of_games(player):
    teams = Team.objects.filter(members__player=player)
    return (
        Match.objects.filter(Q(winner_team__in=teams) | Q(loser_team__in=teams))
        .distinct()
        .count()
    )


def _get_player_current_elo(player):
    current_elo = PlayerRanking.objects.filter(player=player).first()
    return current_elo.elo if current_elo else None


def _get_highest_elo(player):
    return (
        PlayerRanking.objects.filter(player=player)
        .order_by("-elo")
        .values_list("elo", flat=True)
        .first()
    )

def _get_player_current_teams(player):
    return Team.objects.filter(members__player=player, is_active=True).distinct()