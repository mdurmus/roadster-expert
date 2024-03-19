from . import views
from django.urls import path

urlpatterns=[
    path('', views.Home.as_view(), name='home'),
    path('search/', views.search, name="search"),
    path('categories_posts/<str:cats', 
         views.categories_view, name='vehicle_posts')
]