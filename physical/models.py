from django.db import models
from users.models import User, Area

# Create your models here.
class Desktop(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    asset_number = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    disk_serialnumber = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

class Laptop(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    asset_number = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    disk_serialnumber = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

class Hard_Disk(models.Model):
    serialnumber = models.AutoField(primary_key=True)
    size_gb = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serialnumber
