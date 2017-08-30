# Copy-Paste from wagtailsearch
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
# Create your views here.
def home(request):
        context = {'page.welcomeMessage': "Welcome to Django and Wagtail!"}
        return render(request, 'home.html', context)
