from django.urls import path
from . import views

app_name = "records"

urlpatterns = [
    path("", views.index, name="index"),
    path("appointment/create", views.app_create_view, name="app_create"),
]