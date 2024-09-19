from django.db import models
from django.contrib.auth.models import AbstractUser
from app_modules.base.models import BaseModel

class User(AbstractUser, BaseModel):
    
    SUPER_ADMIN = "super admin"
    ADMIN = "admin"
    STUDENT = "student"

    USER_ROLE = (
        (SUPER_ADMIN, "Super Admin"),
        (ADMIN, "Admin"),
        (STUDENT, "Admin"),
    )

    email = models.EmailField(('Email'), unique=True)
    full_name = models.CharField(('Full Name'), max_length=50)
    phone = models.CharField(('Phone'), max_length=20, null=True, blank=True)
    image = models.FileField(upload_to='user-profile', null=True)
    role = models.CharField(('Role'), choices=USER_ROLE, max_length=50, default=ADMIN, null=True, blank=True)

    def __str__(self):
        return self.full_name
    