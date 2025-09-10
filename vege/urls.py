from django.urls import path
from . import views

urlpatterns = [
    path("receipes/", views.receipe_list, name="receipe_list"),
    path("departments/", views.department_list, name="department_list"),
    path("students/", views.student_list, name="student_list"),
]
