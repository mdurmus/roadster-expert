from django.contrib import admin
from .models import Category, Vehicle, Comment, VehicleBrand, VehicleModel
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields =('title')

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields=('comment')

@admin.register(Vehicle)
class VehicleAdmin(SummernoteModelAdmin):
    list_display = ('title','slug','status','created_on')
    search_fields = ('brand','title')
    prepopulated_fields = {'slug':('title',)}
    summernote_fields=('summary','content')
    list_display = ('first_name', 'last_name')

admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)