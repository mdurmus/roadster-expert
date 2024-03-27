from django.urls import path
from .views import ExperienceList, my_experiences

urlpatterns = [
    path('experiences/', ExperienceList.as_view(), name='experiences-list'),
    path('my-experiences/<int:user_id>/', my_experiences, name='my-experiences')
]