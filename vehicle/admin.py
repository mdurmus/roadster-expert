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
    prepopulated_fields = {'slug':('title',)}
    summernote_fields=('summary','content')

admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)