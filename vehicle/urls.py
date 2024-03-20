from .views import Home, ListVehicleInCategoryListView, CategoryListView
from django.urls import path

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<int:category_id>/', ListVehicleInCategoryListView.as_view(), name='category_vehicles'), 
]