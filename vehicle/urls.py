from . import views
from .views import Home, ListVehicleInCategoryListView, CategoryListView, about, contact,VehicleDetail
from django.urls import path

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('<slug:slug>/', VehicleDetail.as_view(), name='vehicle_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<str:cat_name>/', ListVehicleInCategoryListView.as_view(), name='category_vehicles'), 
]