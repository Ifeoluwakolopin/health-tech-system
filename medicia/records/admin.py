from django.contrib import admin
from django.contrib.auth.models import User
from .models import Employee, Patient, Appointment, Prescription

admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription)