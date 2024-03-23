from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, ListVehicleInCategoryListView, CategoryListView, about, contact,VehicleDetail
from django.urls import path
from django.contrib import admin

urlpatterns=[
    path('delete_comment/<int:comment_id>', views.delete_comment,
        name='delete_comment'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
        name='edit_comment'),
    path('', Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<str:cat_name>/', ListVehicleInCategoryListView.as_view(), name='category_vehicles'), 
    path('<slug:slug>/', VehicleDetail.as_view(), name='vehicle_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)