from django.test import TestCase
from .forms import AssetForm

# Create your tests here.
class AssetFormTestCase(TestCase):
    def test_asset_form_valid(self):
        form_data = {
            'id': 'Z20012622000622',
            'model': 'Model A',
            'username': '200121600',
            'area': 1,
            'asset_number':'622000622',
            'serial_number':'ABC123',
            'disk_serialnumber':'XYZ456',
        }
        form = AssetForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())