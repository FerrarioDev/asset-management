from django import forms
from .models import Asset, Hard_Disk

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class DiskForm(forms.ModelForm):
    class Meta:
        model = Hard_Disk
        fields = '__all__'
