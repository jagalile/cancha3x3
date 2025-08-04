from django import forms
from .models import City, Court, NewCourt


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["name", "province"]


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = ["name", "city", "latitude", "longitude", "description"]


class NewCourtForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Nombre de la cancha",
            }
        ),
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Nombre de la ciudad",
            }
        ),
    )

    address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "Dirección de la cancha",
            }
        ),
    )

    class Meta:
        model = NewCourt
        fields = ["name", "city", "address"]
