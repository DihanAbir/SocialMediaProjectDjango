from django.contrib import admin
from .models import Group, GroupMembers
admin.site.register(Group)
admin.site.register(GroupMembers)
