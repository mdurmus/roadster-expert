from django.shortcuts import render
from django.views import generic, View 
from django.views.generic import ListView
from .models import *

class Home(generic.TemplateView):
    '''
    Home page view
    '''
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        return context

class CategoryListView(ListView):
    template_name='vehicle/categories.html'
    model = Category
    context_object_name = 'categories'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Category"
        context['categories'] = Category.objects.all().order_by('title')
        return context

    # data filtering.
    def get_queryset(self):
        return Category.objects.all()

class ListVehicleInCategoryListView(ListView):
    '''
    List all vehicle in a category
    '''

    template_name='vehicle/category_vehicles.html'
    model = Vehicle
    context_object_name = 'vehicles'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = self.kwargs['cat_name']
        context['categories'] = Category.objects.all().order_by('title')
        return context

    def get_queryset(self):
        title = self.kwargs['cat_name']
        category = Category.objects.get(title=title)
        return Vehicle.objects.filter(category=category)

class AboutListView(ListView):