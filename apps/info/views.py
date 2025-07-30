from django.shortcuts import render
from apps.competitions.models import Competition
from apps.geo.models import City, Court
from apps.teams.models import Team
from apps.users.models import Player
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    total_users = Player.objects.count()
    total_teams = Team.objects.count()
    total_competitions = Competition.objects.count()
    total_cities = City.objects.count()
    total_courts = Court.objects.count()
    return render(
        request,
        "landing.html",
        {
            "total_users": total_users,
            "total_teams": total_teams,
            "total_competitions": total_competitions,
            "total_cities": total_cities,
            "total_courts": total_courts,
        },
    )

class TermsAndConditionsView(TemplateView):
    template_name = "terms_and_conditions.html"


class PrivacyPolicyView(TemplateView):
    template_name = "privacy_policy.html"