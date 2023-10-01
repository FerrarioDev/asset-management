from django import forms
from .models import User,Area

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'area']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['area_name', 'area_manager']
