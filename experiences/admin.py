from django.contrib import admin
from .models import Experience
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Experience)
class MyExperienceAdmin(SummernoteModelAdmin):
    list_display = ('user','brand','model','title','created_on',)
    search_fields = ('brand','model',)
    list_filter=('created_on',)
    summernote_fields=('content',)
    actions = ['approve_comments']

    def approve_comments(self, request,queryset):
        queryset.update(approved=True)