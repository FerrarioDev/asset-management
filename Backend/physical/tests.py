from django.test import TestCase
from .forms import AssetForm
from users.models import Area, User

class AssetFormTestCase(TestCase):
    def setUp(self):
        # Create a sample User
        User.objects.create(id='200121600', username='sample_user', role='user')

        # Create a sample Area with an associated area manager
        user = User.objects.get(id='200121600')  # Retrieve the created user
        Area.objects.create(id=1, area_name='Sample Area', area_manager=user)

    def test_asset_form_valid(self):
        # Your test code remains unchanged
        form_data = {
            'id': 'Z20012622000622',
            'model': 'Model A',
            'username': '200121600',  # Use a valid user's ID
            'area': 1,                # Use an existing area's ID
            'asset_type': 'desktop',  # Provide a valid asset type
            'asset_number': '622000622',
            'serial_number': 'ABC123',
            'disk_serialnumber': 'XYZ456',
        }
        form = AssetForm(data=form_data)
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid())
