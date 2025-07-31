# apps/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.forms import PlayerCreationForm, PlayerChangeForm
from.models import Player

class PlayerAdmin(UserAdmin):
    add_form = PlayerCreationForm
    form = PlayerChangeForm
    model = Player
    list_display = ['email', 'username', 'reputation_score', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        ("Reputación", {'fields': ('reputation_score',)}),
        ("Avatar", {'fields': ('avatar',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'avatar'),
        }),
    )

admin.site.register(Player, PlayerAdmin)