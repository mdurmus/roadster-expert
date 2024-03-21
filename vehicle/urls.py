from . import views
from .views import Home, ListVehicleInCategoryListView, CategoryListView, about
from django.urls import path

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<str:cat_name>/', ListVehicleInCategoryListView.as_view(), name='category_vehicles'), 
]