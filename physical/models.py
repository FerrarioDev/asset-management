from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DeviceType(models.TextChoices):
    DESKTOP = 'desktop', 'Desktop'
    LAPTOP = 'laptop', 'Laptop'

class Asset(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    model = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_number = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    disk_serialnumber = models.CharField(max_length=255)
    device_type = models.CharField(
        max_length=10,
        choices=DeviceType.choices,
        default=DeviceType.DESKTOP,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
   

class DisposedDevice(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    model = models.CharField(max_length=30)
    asset_number = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    disk_serialnumber = models.CharField(max_length=255)
    device_type = models.CharField(
        max_length=10,
        choices=DeviceType.choices,
        default=DeviceType.DESKTOP,
    )
    image = models.ImageField(upload_to='images/',default="images/default-avatar.png")
    disposed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serial_number


class Hard_Disk(models.Model):
    serialnumber = models.CharField(primary_key=True,max_length=255)
    description = models.CharField(max_length=255)
    size_gb = models.CharField(max_length=255, unique=True)
    reason = models.CharField(max_length=255, default="Disuse")
    image = models.ImageField(upload_to='images/', default="images/default-avatar.png")
    disposed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serialnumber
