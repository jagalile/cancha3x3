from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from apps.users.forms import CustomLoginForm, SignUpForm
from django.contrib.auth import logout


# Create your views here.
class CustomLoginView(LoginView):
    template_name = "login.html"
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy("dashboard:dashboard")


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("dashboard:dashboard")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        CustomLoginView(self.request, user)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        redirect_url = reverse_lazy("users:login")  # o cualquier otra ruta
        response = JsonResponse({}, status=200)
        response["HX-Redirect"] = redirect_url
        return response
