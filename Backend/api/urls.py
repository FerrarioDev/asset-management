from django.urls import path
from . import views

urlpatterns = [
    path('assets/', views.asset_list),
    path('assets/<str:pk>/', views.asset_detail),    
]
