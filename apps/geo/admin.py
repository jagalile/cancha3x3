from django.contrib import admin
from .models import City, Court, NewCourt

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'province')
    search_fields = ('name', 'province')
    list_filter = ('province',)
    ordering = ('province', 'name')

admin.site.register(City, CityAdmin)

class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name', 'city__province')
    list_filter = ('city__name', 'city__province')
    ordering = ('city', 'name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('city')

admin.site.register(Court, CourtAdmin)

class NewCourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'status')
    search_fields = ('name', 'city', 'address', 'status')
    list_filter = ('city', 'status')
    ordering = ('city', 'name')
    
admin.site.register(NewCourt, NewCourtAdmin)