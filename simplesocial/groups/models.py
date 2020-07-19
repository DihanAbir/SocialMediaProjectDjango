from django.db import models
# for slug
# you can use this to make slug without any hassle
from django.utils.text import slugify
import misaka
# MISAKA IS THE PACKAGE THAT ALLOWES US TO
# MWRITE MARKDOWN INSIDE THE FORMS AND USING MODELS
# when you post something with misaka you can post link markdown
# without any problem
from django.urls import reverse
from django.contrib.auth.models import User
# now we import another package that will
# allow us to use custom tags in the template for better use
# you can register you own tag
from django import template
register = template.Library()


# class Group(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(allow_unicode=True, unique=True)
#     description = models.TextField(blank=True, default='')
#     description_html = models.TextField(editable=False, default='', blank=True)
#     members = models.ManyToManyField(User,through="GroupMember")


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    # every time we have to use the primary key
    # insted we are going to use the slug
    # this is the new style
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    # ONE USER CAN BE A MEMBER OF MULTIPLE GROUP
    #  ONE GROUP CAN HAVE MULTIPLE USER
    #  SO ITS A MANY TO MANY RELATIONSHIP
    # and when you make a many to many relationship
    # you need to probide a pivot table with the through="" option
    # to store this information and and connected this two table
    # in many to many way
    # but remember if you dont do that no problem django will
    # automatically create one in the back end
    # in django you dont need to worry about Many to Many relation
    # like the other framework
    members = models.ManyToManyField(User, through="GroupMembers")


# Provide a many-to-many relation by using an intermediary model that
# holds two ForeignKey fields pointed at the two sides of the relation.

# Unless a through model was provided, ManyToManyField will use the
# create_many_to_many_intermediary_model factory to automatically generate the intermediary model.
    # we overrite some method


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # slugfy the slug field
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)

        return super().save(*args, **kwargs)

    # after a successfull post in the model
    # where would you go

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'slug': self.slug})


class GroupMembers(models.Model):
    # a group member consists of the group and its user
    # to how which group is related with which group
    # consider this as a pivot table for the many to many relationship
    group = models.ForeignKey(
        Group, related_name='membership', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='user_groups', on_delete=models.CASCADE)
