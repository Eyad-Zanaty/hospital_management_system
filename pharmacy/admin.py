from django.contrib import admin
from .models import Medicine
# Register your models here.

class MedicineSearch(admin.ModelAdmin):
    search_fields= ['fullname']
    list_filter= ['category', 'strength', 'dosage_form', 'manufacturer']

admin.site.register(Medicine, MedicineSearch)