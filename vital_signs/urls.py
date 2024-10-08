"""
URL configuration for Medical_Atention project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vital_signs'
urlpatterns = [
    path('', views.index, name='index'),

    path('patients', views.table_patients, name='patients'),
    path('patients/patients_form', views.form_patient, name='patients_form'),
    path('patients/edit_patient/<int:patient_id>', views.edit_patient, name='edit_patient'),
    path('patients/patients_detail/<int:patient_id>', views.patients_detail, name='patients_detail'),

    path('vital_signs', views.form_vital_signs, name='vital_signs_form'),

    path("login/", views.CustomLoginView.as_view(), name="login"),
]
