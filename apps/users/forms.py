# apps/users/forms.py
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from .models import Player


class PlayerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Player
        fields = ("username", "email", "reputation_score", "avatar")


class PlayerChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Player
        fields = ("username", "email", "reputation_score", "avatar")


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Tu apodo en la cancha, cómo te conocerán todos",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "input",
                "placeholder": "Tu correo para no perderte nada",
            }
        ),
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Elige algo seguro para proteger tu cuenta",
            }
        ),
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Repetir contraseña",
            }
        ),
    )

    class Meta:
        model = Player
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "Nombre de Jugador",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Contraseña",
            }
        )
    )
