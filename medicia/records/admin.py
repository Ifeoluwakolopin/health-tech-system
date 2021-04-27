from django.contrib import admin
from .models import Employee, Patient, User, Appointment, Prescription

admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Prescription)