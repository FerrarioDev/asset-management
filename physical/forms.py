from django import forms 
from .models import Desktop, Laptop, Hard_Disk

ASSETS_LIST = [('desktop', 'Desktop'), ('laptop', 'Laptop')]

class AssetForm(forms.ModelForm):
    asset_type = forms.ChoiceField(
        choices=ASSETS_LIST,
        initial ='desktop'
        )

    class Meta:
        model = Desktop
        fields = '__all__'
    
    def clean(self):
        cleaned_data = super().clean()
        asset_type = cleaned_data.get('asset_type')

        if asset_type == 'desktop':
            self._meta.model = Desktop
        elif asset_type == 'laptop':
            self._meta.model = Laptop
        
        return cleaned_data

class DiskForm(forms.ModelForm):
    class Meta:
        model = Hard_Disk
        fields = ['serialnumber', 'size_gb']
        