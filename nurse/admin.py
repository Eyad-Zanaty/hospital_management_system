from django.contrib import admin
from .models import Nurse
# Register your models here.

class NurseSearch(admin.ModelAdmin):
    search_fields= ['fullname', 'phone_number']
    list_filter= ['department', 'shift_type']