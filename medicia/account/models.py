from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ("doctor", "Doctor"),
    ("hr", "HR")
)

class User(AbstractUser):
    type = models.CharField(choices=ROLES, max_length=12)

    def is_doctor(self):
        return self.type=="doctor"

    def is_HR(self):
        return self.type=="hr"

    class Meta:
        ordering=("-id",)