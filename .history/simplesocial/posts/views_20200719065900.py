from django.shortcuts import render


from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from braces.views import SelectRelatedMixin

from .models import Post


def get_post_of_user(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(user=logged_in_user)
    return render(request, 'posts/post_list.html', {'posts': logged_in_user_posts})
