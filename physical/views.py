from django.shortcuts import render, redirect
from .forms import DesktopForm, LaptopForm
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
