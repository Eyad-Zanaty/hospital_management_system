from django.contrib import admin
from .models import Laboratory
# Register your models here.

class LaboratorySearch(admin.ModelAdmin):
    search_fields= ['test_name', 'test_category']
    list_filter= ['test_category']

admin.site.register(Laboratory, LaboratorySearch)