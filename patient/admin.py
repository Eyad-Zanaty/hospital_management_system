from django.contrib import admin
from .models import Patient
# Register your models here.

class PatientSearch(admin.ModelAdmin):
    search_fields= ['fullname', 'phone']
    list_filter= ['gender']

admin.site.register(Patient, PatientSearch)