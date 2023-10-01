from django.db import models
from users import Users, Area

# Create your models here.
class Desktop(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30)
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    asset_number = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    disk_serialnumber = models.CharField(max_length=255)
    created_at = models.DateTimeField()

class Laptop(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=30)
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    asset_number = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    disk_serialnumber = models.CharField(max_length=255)
    created_at = models.DateTimeField()
