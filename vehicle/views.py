from django.contrib.messages.views import SuccessMessageMixin
from .forms import CommentForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (
    render, get_object_or_404, reverse, redirect, resolve_url)
from django.views import generic, View 
from django.views.generic import ListView, UpdateView
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

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
    paginate_by = 4

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
    return render(request, 'vehicle/contact.html',context)

class VehicleDetail(View):
    '''
    Render post details
    '''

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        print(slug)
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
                "page_name": vehicle.title,
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Vehicle.objects.filter(status=1)
        vehicle = get_object_or_404(queryset, slug=slug)
        comments = vehicle.vehicle_comments.filter(approved=True).order_by("-created_on")
        comments_count = Comment.objects.filter(vehicle=vehicle).count()
        liked = False
        if vehicle.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.vehicle = vehicle
            comment.save()
            messages.success(request, """
            Your comment was sent successfully and is awaiting approval!""")
        else:
            comment_form = CommentForm()

        return render(
            request,
            "vehicle/vehicle_detail.html",
            {
                "vehicle": vehicle,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
                'comments_count': comments_count,
            },
        )

class EditComment(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = 'vehicle/edit_comment.html'
    form_class = CommentForm
    success_message = 'The comment was successfully updated'


    def get_success_url(self):
       return reverse('vehicle-detail', args=[self.object.vehicle.slug])

@login_required
def delete_comment(request, comment_id):
    """
    Delete comment
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'The comment was deleted successfully')
    return HttpResponseRedirect(reverse(
        'vehicle-detail', args=[comment.vehicle.slug]))

class PostLike(View):
    '''
    For like a vehicle 
    '''
    def post(self, request, slug):
        vehicle = get_object_or_404(Vehicle, slug=slug)

        if vehicle.likes.filter(id=request.user.id).exists():
            vehicle.likes.remove(request.user)
            messages.warning(request, 'Unliked!')
        else:
            vehicle.likes.add(request.user)
            messages.success(request,'Liked')

        return HttpResponseRedirect(reverse('vehicle_detail', args=[slug]))

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect(reverse('my-profile'))
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'page_name':'Your profile'
    }
    return render(request, 'vehicle/profile.html',context,)

def searchform(request, **kwargs):
    """
    search
    """
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        search_result = Vehicle.objects.filter(Q(title__icontains = search_query) | 
                                               Q(summary__icontains = search_query))

        context = {
            'search_query':search_query,
            'search_results': search_result
        }

        return render(request, 'vehicle/search.html', context)
    
    elif request.method == 'GET':
        return render(request, 'vehicle/search.html')