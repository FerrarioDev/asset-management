from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    created_at = models.DateTimeField()

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=255)
    area_manager = models.ForeignKey(User, on_delete=models.CASCADE)
