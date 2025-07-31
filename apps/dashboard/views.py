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
