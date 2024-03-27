from . import views
from django.urls import path

urlpatterns = [
    path('experiences/', ExperienceList.as_view(), name='experiences-list'),
    path('myexperiences/<int:id>/', MyExperiences.as_view(), name='my-experiences')
]