from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from django.conf import settings


class SignupPageView(View):
    form_class = SignUpForm
    template = "authentication/signup.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            return render(request, self.template, {"form": form})
