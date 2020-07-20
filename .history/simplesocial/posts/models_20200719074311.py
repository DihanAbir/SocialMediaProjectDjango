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
        # this related name is very important
        # this post will be called from the group
        # as group.posts
        Group, related_name="posts", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    # AFTER SUccessfully POSTING THIS MODEL
    # WHERE THE LINK GOES

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
