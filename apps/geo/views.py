from django.conf import settings
from django.shortcuts import render

from apps.geo.models import City, Court


# Create your views here.
def cities(request):
    cities = City.objects.all()
    return render(request, "geo.html", {"cities": cities})


def courts(request):
    courts = Court.objects.all()

    return render(
        request,
        "geo.html",
        {
            "courts": courts,
            "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
        },
    )
