from django.contrib import admin

# Register your models here.
from .models import VideoInfo, Teacher, Category


@admin.register(VideoInfo)
class VideoInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'video_length']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'tname', 'teacher_class', 'dob', 'gender', 'married']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'image', 'details']
