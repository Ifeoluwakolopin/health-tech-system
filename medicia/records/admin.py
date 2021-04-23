from django.contrib import admin
from .models import Employee, Patient

admin.site.register(Employee)
admin.site.register(Patient)