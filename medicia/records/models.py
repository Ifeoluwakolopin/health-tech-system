from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

ROLES = (
    ("doctor", "Doctor"),
    ("hr", "HR")
)

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

class User(AbstractUser):
    type = models.CharField(choices=ROLES, max_length=12)

    def is_doctor(self):
        return self.type=="doctor"

    def is_HR(self):
        return self.type=="hr"

    class Meta:
        ordering=("-id",)

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    phone_validator = RegexValidator(regex="^\+\d{9,15}$", message="Phone number should be in format +1234567890 (up to 15 digits)")
    phone = models.CharField(validators=[phone_validator], max_length=17, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    genotype = models.CharField(max_length=2, choices=GENOTYPES, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    allergies  = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True)
    med_reps = models.FileField(upload_to="patient/reports", blank=True)

    class Meta:
        ordering =  ("-id",)

    def __str__(self):
        return self.first_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_validator = RegexValidator(regex="^\+\d{9,15}$", message="Phone number should be in format +1234567890 (up to 15 digits)")
    phone = models.CharField(validators=[phone_validator], max_length=17, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    status = models.CharField(choices=(("active", "Active"), ("inactive", "Inactive")), blank=True, null=True, max_length=8)
    salary = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=500, blank=True)
    attendance = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.user.first_name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name="appointments", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Employee, related_name="appointments", on_delete=models.CASCADE)
    time_of_visit = models.DateTimeField()
    status = models.CharField(choices=(("pending", "Pending"), ("completed", "Completed")), max_length=9)

    def __str__(self):
        return f"{self.time_of_visit}: Appointment -> Patient: {self.patient} -> Doctor: {self.doctor}"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, related_name="prescriptions", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Employee, related_name="prescriptions", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    symptoms = models.CharField(max_length=250)
    prescription = models.TextField()

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f"{self.date}: Prescription -> Patient: {self.patient} -> Doctor: {self.doctor}"