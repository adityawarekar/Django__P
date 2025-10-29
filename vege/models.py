from django.db import models
from django.conf import settings



class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class Receipe(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipes/")
    receipe_view_count = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

   
    objects = ActiveManager()
    
    admin_objects = models.Manager()

    def __str__(self):
        return self.receipe_name

    class Meta:
        ordering = ["receipe_name"]


class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ["department"]


class StudentID(models.Model):
    student_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.student_id


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name

    class Meta:
        ordering = ["student_name"]
        verbose_name = "Student"


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name="subjectmarks", on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.student_name} - {self.subject.subject_name} ({self.marks})"

    class Meta:
        unique_together = ["student", "subject"]
