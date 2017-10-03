from django.db import models
from wagtail.wagtailcore.models import Page
from django.shortcuts import render

def home(request):
    context = {'devMessage': 'Welcome to dezentrale e.V.!\nThe Website is currently\
    in development! This is a new test'}
    return render(request, 'home_page.html', context)
