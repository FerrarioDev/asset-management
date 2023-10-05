from django.db import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
    username = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=255)
    area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='users_area', null=True, blank=True)  # Reference to Area model
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=255, unique=True)
    area_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='areas_managed')  # Reference to User model
    
    def __str__(self):
        return self.area_name
