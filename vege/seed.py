from faker import Faker
import random
from .models import Department, Student, StudentID, Subject, SubjectMarks

fake = Faker()



def seed_subjects():
    subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]
    for sub in subjects:
        Subject.objects.get_or_create(subject_name=sub)
    print("✅ Subjects created successfully.")



def seed_db(n=10) -> None:
    departments_objs = Department.objects.all()

    if not departments_objs.exists():
        print("⚠️ No departments found. Please add departments before seeding students.")
        return

    for i in range(n):
        try:
            department = random.choice(departments_objs)

          
            student_id = f"STU-{random.randint(1000, 9999)}"
            while StudentID.objects.filter(student_id=student_id).exists():
                student_id = f"STU-{random.randint(1000, 9999)}"

            student_name = fake.name()
            student_email = fake.unique.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )

            print(f"✅ Student {student_name} created successfully.")

        except Exception as e:
            print(f" Error creating student {i+1}: {e}")



def create_subject_marks(n=None):
    try:
        student_objs = Student.objects.all()
        if n:
            student_objs = student_objs[:n]  

        subjects = Subject.objects.all()
        if not subjects.exists():
            print("⚠️ No subjects found. Please run seed_subjects() first.")
            return

        for student in student_objs:
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0, 100)
                )
            print(f" Marks created for {student.student_name}")

    except Exception as e:
        print(f" Error creating subject marks: {e}")
