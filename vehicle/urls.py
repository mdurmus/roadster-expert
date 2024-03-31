from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (Home, ListVehicleInCategoryListView,
                    CategoryListView, about,
                    contact, VehicleDetail,
                    PostLike, Profile)
from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('vehicle-detail/<slug:slug>/',
         views.VehicleDetail.as_view(),
         name='vehicle-detail'),

    path('search/',
         views.searchform,
         name='search_form'),

    path('profile/',
         views.profile,
         name='my-profile'),

    path('like/<slug:slug>/',
         views.PostLike.as_view(),
         name="post_like"),

    path('delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),

    path('edit_comment/<int:pk>/',
         views.EditComment.as_view(),
         name='edit_comment'),

    path('',
         views.Home.as_view(),
         name='home'),

    path('about/',
         views.about,
         name='about'),

    path('contact/',
         views.contact,
         name='contact'),

    path('categories/',
         views.CategoryListView.as_view(),
         name='categories'),

    path('category/<str:cat_name>/',
         views.ListVehicleInCategoryListView.as_view(),
         name='category_vehicles'),
]
