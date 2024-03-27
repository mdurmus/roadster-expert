from django.shortcuts import render
form .models import Experience

class ExperienceList(generic.View):
    model = Experience
    template_name='experiences/experiences_list.html'
    context = {'page_name':'All Experiences'}
    context_object_name = 'experiences'

    def get_queryset(self):
        return Experiences.objects.filter(approved=True)
