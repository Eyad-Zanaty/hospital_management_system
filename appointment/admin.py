from django.contrib import admin
from .models import Appointment
from datetime import datetime
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

# Register your models here.

class AppointmentSearch(admin.ModelAdmin):
    list_filter= [('date', DateRangeFilterBuilder()) ,
        ('time', DateRangeQuickSelectListFilterBuilder()),
        'status',
        ('reminder_time', DateRangeQuickSelectListFilterBuilder())
        ]


admin.site.register(Appointment, AppointmentSearch)