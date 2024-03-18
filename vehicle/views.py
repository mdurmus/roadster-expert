from django.shortcuts import render
from django.views import generic, View 

class Home(generic.TemplateView):
    '''
    Home page view
    '''
    template_name='index.html'