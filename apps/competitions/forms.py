from django import forms
from .models import Competition, Match

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'description', 'city', 'competition_type', 'is_official', 'start_date', 'end_date']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['competition', 'team_a', 'team_b', 'round', 'date', 'court', 'score_team_a', 'score_team_b', 'winner', 'is_verified']
