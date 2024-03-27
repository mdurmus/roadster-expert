from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Experience

class ExperienceList(generic.ListView):
    model = Experience
    template_name='experiences/experience_list.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        return Experience.objects.filter(approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'All Experiences'
        return context

def my_experiences(request, user_id):
    user_experiences = Experience.objects.filter(user_id=user_id, approved=True)
    return render(request, 'experiences/experience_detail.html', 
                  {'experience_list': user_experiences, 
                  'page_name': 'Experiences Detail'})