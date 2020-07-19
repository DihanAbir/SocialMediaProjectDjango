from django.db import models
# we use the user builtin model
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(
        User, related_name='user_profile', on_delete=models.CASCADE)

    def __str__(self):
        return "@{}".format(self.user)
