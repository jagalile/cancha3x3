# apps/users/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from.models import Player

class PlayerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Player
        fields = ('username', 'email', 'reputation_score')

class PlayerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Player
        fields = ('username', 'email', 'reputation_score')