
from django.urls import path
from . import views
app_name = "posts"

urlpatterns = [
    path('', views.get_post_of_user, name="get_post_of_user"),
    path('new/', views.create_post, name="create_post"),

]
