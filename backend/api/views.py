from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view    
from rest_framework import status

from .serializers import AssetSerializer, HardDiskSerializer
from physical.models import Asset, Hard_Disk

@api_view(['GET','POST'])
def asset_list(request):
    if request.method == 'GET':
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def asset_detail(request, pk):
    try:
        asset = Asset.objects.get(pk=pk)
    except Asset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)