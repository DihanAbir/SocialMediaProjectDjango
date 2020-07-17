from django.shortcuts import render
from .forms import RegistrationForm, ProfileChange
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def signup_user(request):
    form = RegistrationForm()
    registered = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        registered = True
    # when the page loads
    fdct = {'form': form, 'registered': registered}
    return render(request, 'accounts/signup.html', fdct)
