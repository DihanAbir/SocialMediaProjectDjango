from django import forms
from django.contrib.auth.models import User
# for user creation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import UserProfile


class RegistrationForm(UserCreationForm):
    # adding an extra field
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileChange(UserChangeForm):

    class Meta:
        model = User

        # adding all the field avilable for changing
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
