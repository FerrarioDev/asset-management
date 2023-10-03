from django.urls import path
from . import views

urlpatterns = [
    path('add_desktop/', views.add_desktop, name='add_desktop'),
    path('add_laptop/', views.add_laptop, name='add_laptop'),
    path('disk_disposal/', views.disk_disposal, name='disk_disposal'),
]
