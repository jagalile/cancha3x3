from django.contrib import admin
from .models import PlayerRanking

# Register your models here.
class PlayerRankingAdmin(admin.ModelAdmin):
    list_display = ('player', 'elo', 'date')
    search_fields = ('player__username',)
    ordering = ('-elo',)

admin.site.register(PlayerRanking, PlayerRankingAdmin)
