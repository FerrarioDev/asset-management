from django.shortcuts import render, redirect
from .forms import UserForm, AreaForm

# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def add_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area_list')
    else:
        form = AreaForm()
    return render(request, 'add_area.html', {'form': form})
