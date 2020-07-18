from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    # if you give the name just login in the name=
    # some additional benigfits you have
    # like login redirect
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.signup_user, name="signup"),
]
