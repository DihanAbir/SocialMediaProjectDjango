from django.db import models
# we use the user builtin model
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin


# you can directly use the user
# no need to go for this hassle
class User(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
