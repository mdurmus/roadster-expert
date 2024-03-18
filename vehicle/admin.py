from django.contrib import admin
from .models import Category, Vehicle, Comment, VehicleBrand, VehicleModel
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name','email','short_comment',)
    search_fields = ('email','name',)
    list_filter = ('created_on',)
    summernote_fields=('comment')
    actions = ['approve_comments']

    def short_comment(self, obj):
        return obj.comment[:50]+'...' if obj.comment else ''
    short_comment.short_description = 'Comment'

    def approve_comments(self,request,queryset):
        queryset.update(approved=True)


@admin.register(Vehicle)
class VehicleAdmin(SummernoteModelAdmin):
    list_display = ('category','brand','model','status')
    search_fields = ('brand__brand','model__model')
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','created_on')
    summernote_fields=('summary','content')


admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(Category)
