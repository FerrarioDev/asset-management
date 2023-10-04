from django.shortcuts import render, redirect
from .forms import DiskForm, AssetForm
# Create your views here.

def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')  # Change 'asset_list' to your asset list URL
    else:
        form = AssetForm()
    return render(request, 'add_asset.html', {'form': form})

def disk_disposal(request):
    if request.method == 'POST':
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drive_list')
    else:
        form = DiskForm()
    return render(request, 'disposal.html', {'form': form})

