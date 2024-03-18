from django.contrib import admin
from .models import Courses, Speciality

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("title", "total_course")


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "active_students", "durection", "price", "rayting", "status", "create_date")
