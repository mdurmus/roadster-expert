from django.shortcuts import render
from django.views import generic, View 
from .models import *
from django.db.models import Q

class Home(generic.TemplateView):
    '''
    Home page view
    '''
    template_name='index.html'

