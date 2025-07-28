from django import forms
from .models import Team, TeamMember

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'is_active']

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['team', 'user', 'is_captain']
