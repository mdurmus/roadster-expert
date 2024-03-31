from django import forms
from .models import Experience
from django_summernote.widgets import SummernoteWidget


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['brand', 'model', 'title', 'summary',
                  'content', 'max_speed', 'featured_image']


class UpdateExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['brand', 'model', 'title',
                  'summary', 'content', 'max_speed']
        widgets = {'content': SummernoteWidget(), }
