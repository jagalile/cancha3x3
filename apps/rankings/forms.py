from django import forms
from .models import PlayerRanking

class PlayerRankingForm(forms.ModelForm):
    class Meta:
        model = PlayerRanking
        fields = ['player', 'elo']
