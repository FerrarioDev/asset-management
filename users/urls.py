from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('add_area/', views.add_area, name='add_area'),
]
