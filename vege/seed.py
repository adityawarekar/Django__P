from faker import Faker
import random
from .models import Department, Student, StudentID

fake = Faker()

def seed_db(n=10) -> None:
    departments_objs = Department.objects.all()

    if not departments_objs.exists():
        print("No departments found. Please add departments before seeding students.")
        return

    for i in range(n):
        try:
            department = random.choice(departments_objs)  # safer than randint

            student_id = f"STU-{random.randint(100, 999)}"
            student_name = fake.name()
            student_email = fake.unique.email()  # ensures no duplicate emails
            student_age = random.randint(20, 30)
            student_address = fake.address()

            # Create StudentID
            student_id_obj = StudentID.objects.create(student_id=student_id)

            # Create Student
            Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )

            print(f"Student {student_name} created successfully.")

        except Exception as e:
            print(f"Error creating student {i+1}: {e}")
