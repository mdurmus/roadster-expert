from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Experience
from .forms import ExperienceForm, UpdateExperienceForm


class ExperienceList(generic.ListView):
    """
    View listing user experiences.
    """
    model = Experience
    template_name = 'experiences/experience_list.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        user = self.request.user
        return Experience.objects.filter(approved=True) \
                                 .exclude(user=user) \
                                 .order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'All Experiences'
        return context


def my_experiences(request, user_id):
    """
    View displaying logged-in user experiences.
    """
    user_experiences = Experience.objects.filter(user_id=user_id,
                                                 approved=True)
    return render(
        request,
        'experiences/my_experiences.html',
        {
            'experiences': user_experiences,
            'page_name': 'My Experiences'
        }
    )


def experience_detail(request, exp_id):
    """
    View displaying the details of a single experience.
    """
    experience = get_object_or_404(Experience, id=exp_id)
    return render(
        request,
        'experiences/experience-detail.html',
        {
            'experience': experience,
            'page_name': 'Experience Detail'
        }
    )


def create_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('experiences-list')
    else:
        form = ExperienceForm()

    return render(
        request,
        'experiences/create_experience.html',
        {
            'form': form,
            'page_name': 'Create Experience'
        }
    )


def update_experience(request, exp_id):
    experience = get_object_or_404(Experience, id=exp_id)

    if request.method == 'POST':
        form = UpdateExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experience-detail', exp_id=exp_id)
    else:
        form = UpdateExperienceForm(instance=experience)

    return render(
        request,
        'experiences/update-experience.html',
        {
            'form': form,
            'page_name': 'Update Experience'
        }
    )
