from django import forms
from .models import City, Court

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'province']

class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ['name', 'city', 'address', 'description']
