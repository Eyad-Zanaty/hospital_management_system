from .models import User
from django import forms

class UserSearchForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'role', 'gender']