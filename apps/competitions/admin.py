from django.contrib import admin
from .models import Competition, Match

# Register your models here.
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'competition_type', 'city__name', 'city__province', 'start_date', 'end_date', 'is_official')
    search_fields = ('name', 'city')
    list_filter = ('competition_type', 'is_official', 'city__name', 'city__province')
    ordering = ('start_date',)

admin.site.register(Competition, CompetitionAdmin)

class MatchAdmin(admin.ModelAdmin):
    list_display = ('competition', 'round', 'date', 'court', 'winner_team', 'score_winner_team', 'loser_team', 'score_loser_team', 'is_verified')
    search_fields = ('competition__name', 'court__name')
    list_filter = ('competition__name', 'court', 'is_verified')
    ordering = ('date',)

admin.site.register(Match, MatchAdmin)
