from django.urls import path
from .views import (ExperienceList, my_experiences,
                    experience_detail, create_experience,
                    update_experience)

urlpatterns = [
    path(
        'update-experience/<int:exp_id>/',
        update_experience,
        name='update-experience'
    ),

    path(
        'create-experience',
        create_experience,
        name='create-experience'
        ),

    path(
        'experiences/',
        ExperienceList.as_view(),
        name='experiences-list'),

    path(
        'my-experiences/<int:user_id>/',
        my_experiences,
        name='my-experiences'),

    path(
        'experience-detail/<int:exp_id>',
        experience_detail,
        name='experience-detail'),
]
