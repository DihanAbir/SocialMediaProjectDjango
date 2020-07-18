from django.views.generic import TemplateView
from django.shortcuts import redirect


def HomePage(request):
    return redirect('groups:list_group')
