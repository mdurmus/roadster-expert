from . import views
from django.urls import path

urlpatterns = [
    path('experiences/', ExperienceList.as_view(), name='experiences-list'),
]