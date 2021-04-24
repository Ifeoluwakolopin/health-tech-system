from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    ROLES = (
        ("doctor", "Doctor"),
        ("pharmacist", "Pharmacist"),
        ("nurse", "Nurse"),
        ("paramedic", "Paramedic"),
        ("non-medic", "Non-medic")
    )
    _id = models.AutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=16)
    role = models.CharField(max_length=100, choices=ROLES, default="doctor")
    employed = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("_id",)

    def __str__(self):
        return f"{self._id} - {self.first_name} {self.last_name}"

class Patient(models.Model):
    GENOTYPES = (
        ("AA", "AA"),
        ("AS", "AS"),
        ("SS", "SS"),
        ("AC", "AC"),
        ("SC", "SC"),
        ("CC", "CC")
    )

    BLOOD_GROUPS = (
        ("A+", "A-positive"), ("A-", "A-negative"),
        ("B+", "B-positive"), ("B-", "B-negative"),
        ("O+", "O-positive"), ("O-", "O-negative"),
        ("AB+", "AB-positive"), ("AB-", "AB-negative")
    )
    _id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    # Physical Information
    height = models.PositiveIntegerField(default=1)
    weight = models.PositiveIntegerField(default=1)
    genotype = models.CharField(max_length=2, choices=GENOTYPES)
    bg = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    gender = models.CharField(max_length=40)
    allergies = models.CharField(max_length=250, null=True)

    class Meta:
        ordering =  ("_id",)

    def __str__(self):
        return f"{self._id} - {self.first_name}"


