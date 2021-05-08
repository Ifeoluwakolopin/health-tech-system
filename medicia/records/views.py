from django.shortcuts import get_object_or_404, render
from .models import Patient, Employee, Appointment, Prescription
from .forms import AppointmentCreateForm, PrescriptionCreateForm


def index(request):
    return render(request, "records/index.html")

def app_create_view(request):
    if request.method == "POST":
        app_form = AppointmentCreateForm(request.POST)
        if app_form.is_valid():
            appointment = app_form.save()
            return render(request, "records/appointment/created.html", {"app":appointment})
    else:
        app_form = AppointmentCreateForm()
    return render(request, "records/appointment/create.html", {"app_form":app_form})
