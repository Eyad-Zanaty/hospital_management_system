from django.contrib import admin
from .models import Billing
# Register your models here.
class BillingSearch(admin.ModelAdmin):
    search_fields = ['payment_id']
    list_filter= ['payment_status']

admin.site.register(Billing, BillingSearch)