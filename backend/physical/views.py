from django.shortcuts import  get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from .forms import DiskForm, AssetForm


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
