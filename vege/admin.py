from django.contrib import admin
from .models import Receipe, Department, Student


from .models import *

@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ("receipe_name", "user", "receipe_view_count")

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department",)

@admin.register(StudentID)
class StudentIDAdmin(admin.ModelAdmin):
    list_display = ("student_id",)    

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_name", "student_id", "student_email", "department")
    search_fields = ("student_name", "student_id", "student_email")
    list_filter = ("department",)        
