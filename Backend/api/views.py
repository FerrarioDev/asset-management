from django.shortcuts import render
from rest_framework import generics
from physical.models import Asset, Hard_disk
from .serializers import AssetSerializer, HardDiskSerializer

# Create your views here.
class AssetListCreateView(generics.listCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class HardDiskListCreateView(generics.listCreateAPIView):
    queryset = Hard_disk.objects.all()
    serializer_class = HardDiskSerializer

class HardDiskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hard_disk.objects.all()
    serializer_class = HardDiskSerializer