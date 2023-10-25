from django import forms
from .models import Asset, Hard_Disk

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['id', 'model','user','asset_number','serial_number', 'disk_serialnumber', 'location','device_type']

class DiskForm(forms.ModelForm):
    class Meta:
        model = Hard_Disk
        fields = '__all__'

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
