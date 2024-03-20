from .views import Home, CategoryListView
from django.urls import path

urlpatterns=[
    path('', Home.as_view(), name='home'),
     path('category/<int:category_id>/', CategoryListView.as_view(), name='category_vehicles'),
]