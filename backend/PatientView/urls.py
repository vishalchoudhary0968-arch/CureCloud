from django.urls import path

from . import views

urlpatterns = [
    path("list", views.PatientList),
    path("create", views.PatientCreate),
    path("update/<int:id>", views.PatientUpdate),
    path("delete/<int:id>", views.PatientDelete),

]
