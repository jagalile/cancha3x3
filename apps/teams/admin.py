from django.contrib import admin
from .models import Team, TeamMember

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)
    ordering = ('name',)

admin.site.register(Team, TeamAdmin)

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('team', 'player', 'join_date', 'leave_date', 'is_captain')
    search_fields = ('team__name', 'player__username')
    list_filter = ('team', 'is_captain')
    ordering = ('team', 'player')
    readonly_fields = ('join_date',)

admin.site.register(TeamMember, TeamMemberAdmin)
