from django.shortcuts import render
form .models import Experience

class ExperienceList(generic.ListView):
    model = Experience
    template_name='experiences/experiences_list.html'
    context = {'page_name':'All Experiences'}
    context_object_name = 'experiences'

    def get_queryset(self):
        return Experiences.objects.filter(approved=True)

class MyExperiences(DetailView):
    model = Experience
    template_name = 'experiences/experiences_detail.html'
    context = {'page_name':'Experiences Detail'}
    context_object_name = 'experience'
    