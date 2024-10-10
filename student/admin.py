from django.contrib import admin
from student import models
# Register your models here.

@admin.register(models.student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('full_name','date_of_birth')

@admin.register(models.book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','start_date','end_date')

@admin.register(models.passport)
class PassportAdmin(admin.ModelAdmin):
    list_display=('full_name','series_number')

@admin.register(models.course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('title','hours')

@admin.register(models.curator)
class CuratorAdmin(admin.ModelAdmin):
    list_display=('full_name','department')