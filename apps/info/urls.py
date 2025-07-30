from django.urls import path

from . import views

app_name = "info"

urlpatterns = [
    path("", views.index, name="index"),
    path("terms-and-conditions/", views.TermsAndConditionsView.as_view(), name="terms_and_conditions"),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name="privacy_policy"),
]
