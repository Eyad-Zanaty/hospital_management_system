from django.contrib import admin
from .models import User
from .forms import UserSearchForm
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'role', 'phone_number', 'gender', 'date_of_birth', 'address', 'employee_id', 'job_title', 'data_joined')
    search_fields = ('first_name', 'last_name', 'email', 'role', 'phone_number', 'gender', 'job_title')
    form = UserSearchForm
    list_filter= ('role', 'gender')
    
admin.site.register(User, UserAdmin)