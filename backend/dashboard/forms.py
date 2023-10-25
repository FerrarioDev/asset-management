from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a group",
        required=True,
        widget=forms.Select(attrs={'class':'form-control'}),
    )

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2','group')