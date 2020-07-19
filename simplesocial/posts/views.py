from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Post
from .forms import PostForm


def get_post_of_user(request):
    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(user=logged_in_user)
    return render(request, 'posts/post_list.html', {'posts': logged_in_user_posts})


# SelectRelatedMixin will fetch the related group only
# in the form
# login Required Mixin checks for logged in  user
# and generic will create a generic view form

class CreatePostView(LoginRequiredMixin, CreateView):
    # login mixin wants wo know
    # where they will prompt you for login
    # so provide a url
    login_url = '/login/'
    # after login where they will redirect
    # this variable name cant be changed
    redirect_field_name = 'groups/group_list.html'
    # for creating you need a form
    form_class = PostForm
    template_name = "posts/post_form.html"

    # WHY ADDING THIS ?
    # IN THE MODELS WE HAVE THREE FIELD THAT CANT BE NULL AND HAVE TO
    # BE ADDED .ONE IS THE USER OBJECT BUT WE DONT GIVE USER TO SET THE AUTHOR FIELD
    # THE CURRENT USER WILL BE THE VALUE
    # SO THIS METHOD WE OVERRITE AND SET THE LOGGED USER TO THE CURRENT AUTHOR
    # OTHER WISE THESE FILED WILL BE EMPTY
    # SO WE SET THE VALUE AND THE TITLE AND TEXT WILL BE FILLED WITH USER

    def form_valid(self, form):

        form.instance.user_id = self.request.user.pk
        return super().form_valid(form)
