from django.db import models
from wagtail.wagtailcore.models import Page
from django.shortcuts import render
def default(request):
    context = {'devMessage': 'Welcome to dezentrale e.V.!\nThe Website is currently\
    in development!'}
    return render(request, 'home.html', context)
    
