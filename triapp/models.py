from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class host_UserData(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.BigIntegerField(null=True,unique=True)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username
class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE ,default=1)
    type = models.CharField(max_length=255)
    rental_mode = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    description = models.TextField()
    sleeping_arrangement = models.CharField(max_length=255)
    washrooms = models.CharField(max_length=255)
    images = models.ImageField(upload_to='property/', null=True, blank=True)
    nearest_station_airport = models.CharField(max_length=255)
    nearest_station_bus = models.CharField(max_length=255)
    nearest_station_train = models.CharField(max_length=255)
    photos = models.TextField()
    amenities = models.CharField(max_length=255)
    preferred_guest = models.CharField(max_length=255)
    length_of_stay = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.type} in {self.city}, {self.state}"