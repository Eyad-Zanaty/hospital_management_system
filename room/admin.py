from django.contrib import admin
from .models import Room
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)
# Register your models here.

class RoomSearch(admin.ModelAdmin):
    search_fields= ['number', 'type']
    list_filter= ['type',
    ('admission_date', DateRangeFilterBuilder()),
    ('discharge_date', DateRangeFilterBuilder())
    ]

admin.site.register(Room, RoomSearch)