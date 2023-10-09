from django.urls import path
from . import views

urlpatterns = [
    # home/list of assets
    path('', views.AssetListView.as_view(), name='asset_list'),
    # upload asset
    path('upload/', views.add_asset, name='upload'),
    path('disposal/', views.disk_disposal, name='disposal'),
]
