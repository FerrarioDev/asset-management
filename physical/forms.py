from django import forms
from .models import Desktop, Laptop, Hard_Disk

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = '__all__'

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

class DiskForm(forms.ModelForm):
    class Meta:
        model = Hard_Disk
        fields = '__all__'
