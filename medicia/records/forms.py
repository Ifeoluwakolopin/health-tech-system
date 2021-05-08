from django import forms
from .models import Appointment, Prescription

class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ("patient", "doctor", "time_of_visit", "status")

class PrescriptionCreateForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ("patient", "doctor", "symptoms", "prescription")