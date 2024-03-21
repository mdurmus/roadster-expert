from django.shortcuts import (
    render, get_object_or_404, reverse, redirect, resolve_url)
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
        return context

class CategoryListView(ListView):
    template_name='vehicle/categories.html'
    model = Category
    context_object_name = 'categories'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Category"
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
        return context

    def get_queryset(self):
        title = self.kwargs['cat_name']
        category = Category.objects.get(title=title)
        return Vehicle.objects.filter(category=category)

def about(request):
    '''
    About page
    '''
    context = {'page_name':'About Us'}
    return render(request, 'vehicle/about.html',context)

def contact(request):
    '''
    Contact page
    '''
    context = {'page_name':'Contact Us'}
    return render(request, 'vehicle/contact.html')

class VehicleDetail(View):
    '''
    Render post details
    '''

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        queryset = Vehicle.objects.filter(status=1)
        vehicle = get_object_or_404(queryset, slug=slug)
        comments = Comment.objects.filter(vehicle=vehicle, approved=True).order_by("-created_on")
        comments_count = Comment.objects.filter(vehicle=vehicle).count()
        liked = False
        if vehicle.likes.filter(id=request.user.id).exists():
            liked = True
        
        return render(
            request,
            "vehicle/vehicle_detail.html",
            {
                "vehicle": vehicle,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "comments_count": comments_count,
            },
        )