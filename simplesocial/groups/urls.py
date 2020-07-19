# from django.conf.urls import url

# from . import views

# app_name = 'groups'

# urlpatterns = [
#     url(r"^$", views.ListGroups.as_view(), name="all"),
#     url(r"^new/$", views.CreateGroup.as_view(), name="create"),
#     url(r"^posts/in/(?P<slug>[-\w]+)/$",
#         views.SingleGroup.as_view(), name="single"),
#     url(r"join/(?P<slug>[-\w]+)/$", views.JoinGroup.as_view(), name="join"),
#     url(r"leave/(?P<slug>[-\w]+)/$", views.LeaveGroup.as_view(), name="leave"),
# ]


from django.urls import path
from . import views
app_name = "groups"

urlpatterns = [
    path("", views.ListGroup.as_view(), name='list_group'),
    path("new", views.CreateGroup.as_view(), name="create_group"),
    path("detail/<slug:slug>", views.DetailGrop.as_view(), name='detail'),
    path("join/<slug:slug>", views.join_group, name='join'),
    path("leave/<slug:slug>", views.leave_group, name='leave'),


]
