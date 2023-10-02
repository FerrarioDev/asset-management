from django import forms 
from .models import Desktop, Laptop
class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ['id', 'model', 'username', 'area', 'asset_number', 'disk_serialnumber']
    
class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['id', 'model', 'username', 'area', 'asset_number', 'disk_serialnumber']