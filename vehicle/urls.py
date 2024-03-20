from .views import Home, ListVehicleInCategoryListView, CategoryListView
from django.urls import path

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<str:cat_name>/', ListVehicleInCategoryListView.as_view(), name='category_vehicles'), 
]