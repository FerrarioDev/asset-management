from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetListView.as_view(), name='asset_list'),
    path('upload/', views.add_asset, name='upload'),
    path('disposal/', views.disk_disposal, name='disposal'),
]
