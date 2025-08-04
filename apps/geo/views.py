from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from apps.geo.forms import NewCourtForm
from apps.geo.models import City, Court


# Create your views here.
def cities(request):
    cities = City.objects.all()
    return render(request, "geo.html", {"cities": cities})


def courts(request):
    if request.method == "POST":
        form = NewCourtForm(request.POST)
        if form.is_valid():
            user = request.user
            court = form.save(commit=False)
            court.player = user
            court.save()
            send_mail(
                subject="Solcitud - Nueva Cancha",
                message=f"Cancha: {court.name}\nCiudad: {court.city}\nDirección: {court.address}\nEstado: {court.status}\nJugador: {court.player.id} - {court.player.username} - {court.player.email}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["admin@cancha3x3.es"],  # Puedes agregar más
            )

            return render(request, "court_form.html")
    else:
        form = NewCourtForm()

    courts = Court.objects.all()

    return render(
        request,
        "geo.html",
        {
            "courts": courts,
            "google_maps_api_key": settings.GOOGLE_MAPS_API_KEY,
            "form": form,
        },
    )
