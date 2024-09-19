from django.db import models

from app_modules.base.models import BaseModel
from app_modules.users.models import User

class Student(BaseModel):
    CS = "computer science"
    EC = "electrical engineering"
    CE = "civil engineering"

    DEPARTMENTS = (
        (CS, "Computer Science"),
        (EC, "Electrical Engineering"),
        (CE, "Civil Engineering"),
    )

    BSC = "B.Sc."
    BTECH = "b.tech"
    MTECH = "m.tech"
    MCA = "mca"
    BCA = "bca"

    DEGREES = (
        (BSC, "b.Sc"),
        (BTECH, "b.tech"),
        (MTECH, "m.tech"),
        (BCA, "bca"),
        (MCA, "mca"),
    )

    SEM1 = "1"
    SEM2 = "2"
    SEM3 = "3"
    SEM4 = "4"
    SEM5 = "5"
    SEM6 = "6"
    SEM7 = "7"
    SEM8 = "8"

    SEMESTERS = (
        (SEM1, "1"),
        (SEM2, "2"),
        (SEM3, "3"),
        (SEM4, "4"),
        (SEM5, "5"),
        (SEM6, "6"),
        (SEM7, "7"),
        (SEM8, "8"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_set")
    student_id = models.CharField(("Student ID"), max_length=40)
    department = models.CharField(("Department"), choices=DEPARTMENTS, max_length=200)
    college_email = models.EmailField(("Student Email"), max_length=200)
    semester = models.CharField(("Semester"), choices=SEMESTERS, max_length=10)
    degree = models.CharField(("Degree"), max_length=200, choices=DEGREES)

    def __str__(self):
        return self.user.full_name