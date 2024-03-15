from django.contrib import admin
from .models import Category, Vehicle, Comment, VehicleBrand, VehicleModel
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields =('title')

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('created_on',)
    search_fields = ('email',)
    list_filter = ('created_on',)
    summernote_fields=('comment')
    actions = ['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(approved=True)


@admin.register(Vehicle)
class VehicleAdmin(SummernoteModelAdmin):
    list_display = ('title','slug','status','created_on')
    search_fields = ('brand','title')
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status','created_on')
    summernote_fields=('summary','content')

admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)