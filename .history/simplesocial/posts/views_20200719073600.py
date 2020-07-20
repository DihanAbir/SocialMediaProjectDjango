from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect

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

def create_post(request):
    form = PostForm()
    posted = False
    if request.method == "POST":
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()

            posted = True
            return redirect('groups:list_group')
    # when the page loads
    fdct = {'form': form, 'posted': posted}
    return render(request, 'posts/post_form.html', fdct)
