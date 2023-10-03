from django.shortcuts import render, redirect
from .forms import DesktopForm, LaptopForm, DiskForm
# Create your views here.

def add_desktop(request):
    if request.method == 'POST':
        form = DesktopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desktop_list')
    else:
        form = DesktopForm()
    return render(request, 'add_desktop.html', {'form': form})

def add_laptop(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')
    else:
        form = LaptopForm()
    return render(request, 'add_laptop.html', {'form': form})

def disk_disposal(request):
    if request.method == 'POST':
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drive_list')
    else:
        form = DiskForm()
    return render(request, 'disposal.html', {'form': form})

