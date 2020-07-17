import misaka
from django.db import models
from django.urls import reverse
from groups.models import Group
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        Group, related_name="group", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    # AFTER SPOSTING THIS MODEL
    # WHERE THE LINK GOES

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
