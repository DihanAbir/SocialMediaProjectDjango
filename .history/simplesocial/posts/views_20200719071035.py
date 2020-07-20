from django.shortcuts import render


from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic
# this will be used to fetch the froup in in the form
# only if he is the member of it
from braces.views import SelectRelatedMixin


from .models import Post


def get_post_of_user(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(user=logged_in_user)
    return render(request, 'posts/post_list.html', {'posts': logged_in_user_posts})


# SelectRelatedMixin will fetch the related group only
# in the form
# login Required Mixin checks for logged in  user
# and generic will create a generic view form

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = Post

    def form_valid(self, form):
        # we need to attach the user to the post
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
