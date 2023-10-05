from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import DiskForm, DesktopForm, LaptopForm
from .models import Desktop, Laptop
# Create your views here.

def add_asset(request):
    if request.method == 'POST':
        asset_type = request.POST.get('asset_type')
        desktop_form = DesktopForm(request.POST)
        laptop_form = LaptopForm(request.POST)
        
        if asset_type == 'desktop' and desktop_form.is_valid():
            desktop_form.save()
            return redirect('asset_list')
        elif asset_type == 'laptop' and laptop_form.is_valid():
            laptop_form.save()
            return redirect('asset_list')

    else:
        desktop_form = DesktopForm()
        laptop_form = LaptopForm()
    
    return render(request, 'assets/add_asset.html', {'desktop_form': desktop_form, 'laptop_form': laptop_form})


class AssetListView(ListView):
    template_name = 'assets/home.html'
    def get_queryset(self):
        asset_type = self.request.GET.get('type')
        if asset_type == 'laptop':
            return Laptop.objects.all()
        if asset_type == 'desktop':
            return Desktop.objects.all()
        else:
            return []
        

def disk_disposal(request):
    if request.method == 'POST':
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drive_list')
    else:
        form = DiskForm()
    return render(request, 'assets/disposal.html', {'form': form})

