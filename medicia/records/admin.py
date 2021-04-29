from django.contrib import admin
from .models import Employee, Patient, Appointment, Prescription

admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription)