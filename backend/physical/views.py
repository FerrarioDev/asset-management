from django.shortcuts import  get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .forms import DiskForm, AssetForm, CSVUploadForm
import csv
from .models import Asset


def add_asset(request):
    form = AssetForm() 
    
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            # Save the asset with the specified device type
            device_type = form.cleaned_data.get('device_type')
            form.save()
            return redirect('asset_list')
    
    return render(request, 'assets/add_asset.html', {'form': form})

'''
def add_asset(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'single':
            return add_singleasset(request)
        elif action == 'import':
            return upload_csv(request)

    # For GET requests or other cases, render a form to choose the action.
    form = AssetForm()
    upload_form = CSVUploadForm()
    return render(request, 'assets/add_asset.html', {'form': form, 'upload_form': upload_form})
    
def add_singleasset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            device_type = form.cleaned_data.get('device_type')
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'assets/add_asset.html', {'form': form})

    
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            csv_reader = csv.reader(decoded_file.splitlines(), delimiter=',')
            header = next(csv_reader)
            for row in csv_reader:
                asset_data = {
                    'id': row[0],
                    'model': row[1],
                    'user': row[2],
                    'asset_number': row[3],
                    'disk_serialnumber': row[4],
                    'location': "ph",
                    'device_type': 'desktop',
                }
                Asset.objects.create(**asset_data)
            return redirect('asset_list')
    form = CSVUploadForm()
    return render(request, 'assets/add_asset.html', {'form': form})
'''
def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)
    form = AssetForm(instance=asset)

    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_detail', asset_id=asset_id)

    return render(request, 'assets/asset_detail.html', {'asset': asset, 'form': form})


class AssetListView(ListView):
    model = Asset
    template_name = 'assets/home.html'
    context_object_name = 'assets'

    def get_queryset(self):
        asset_type = self.request.GET.get('type')
        if asset_type in ('laptop', 'desktop'):
            # Filter assets based on device type
            return Asset.objects.filter(device_type=asset_type)
        else:
            return Asset.objects.all()

def disk_disposal(request):
    if request.method == 'POST':
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drive_list')
    else:
        form = DiskForm()
    return render(request, 'assets/disposal.html', {'form': form})
