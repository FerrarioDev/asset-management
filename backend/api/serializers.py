from rest_framework import serializers
from physical.models import Asset, Hard_Disk

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class HardDiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hard_Disk
        fields = '__all__'
        