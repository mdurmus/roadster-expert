from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Experience

class ExperienceList(generic.ListView):
    model = Experience
    template_name='experiences/experience_list.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        user = self.request.user
        return Experience.objects.filter(approved=True).exclude(user=user).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'All Experiences'
        return context

def my_experiences(request, user_id):
    user_experiences = Experience.objects.filter(user_id=user_id, approved=True)
    return render(request, 'experiences/my_experiences.html', 
                  {'experience_list': user_experiences, 
                  'page_name': 'My Experiences'})

def experience_detail(request, exp_id):
    experience = get_object_or_404(Experience, id=exp_id)
    return render(request, 'experiences/experience-detail.html',
                  {'experience' : experience,
                   'page_name':'Experience Detail'})