from django.contrib import admin
from .models import Doctor
# Register your models here.
class DoctorSearch(admin.ModelAdmin):
    search_fields = ['fullname', 'specialization', 'license_number', 'phone_number', 'email']
    list_filter= ['specialization', 'working_days']
    
admin.site.register(Doctor, DoctorSearch)

