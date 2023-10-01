from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='users_area')  # Reference to Area model
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=255)
    area_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='areas_managed')  # Reference to User model
    
    def __str__(self):
        return self.area_name
