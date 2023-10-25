from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group

from .forms import CustomUserCreationForm


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def signup(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group_id = form.cleaned_data['group'].id
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'dashboard/signup.html', {'form':form})