from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class host_UserData(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.BigIntegerField(null=True,unique=True)
    password=models.CharField(max_length=100)
    token=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.username
class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    property_type = models.CharField(max_length=255,null=True)
    number_properties = models.CharField(max_length=255,null=True)
    property_model = models.CharField(max_length=255,null=True)
    property_name = models.CharField(max_length=255,null=True)
    house_number = models.CharField(max_length=255,null=True)
    postal_code = models.CharField(max_length=10,null=True)
    city = models.CharField(max_length=255,null=True)
    landmark = models.CharField(max_length=255,null=True)
    instructions = models.TextField()
    number_of_bedrooms = models.CharField(max_length=255)
    beds = models.CharField(max_length=255)
    living_room = models.CharField(max_length=255,null=True)
    other_spaces = models.CharField(max_length=255,null=True)
    shared_spaces = models.CharField(max_length=255,null=True)
    allowed_guest = models.CharField(max_length=255,null=True)
    bathroom = models.CharField(max_length=255,null=True)
    number_of_bathrooms = models.CharField(max_length=255,null=True)
    no_of_separate_bathrooms = models.CharField(max_length=255,null=True)
    apartment_size = models.CharField(max_length=255,null=True)
    general_amenities = models.CharField(max_length=255,null=True)
    cooking_cleaning_amenities = models.CharField(max_length=255,null=True)
    other_amenities = models.CharField(max_length=255,null=True)
    outside_view = models.CharField(max_length=255,null=True)
    meals_type = models.CharField(max_length=255,null=True)
    free_meals = models.CharField(max_length=255,null=True)
    paid_meals = models.CharField(max_length=255,null=True)
    parking = models.CharField(max_length=255,null=True)
    parking_spots = models.CharField(max_length=255,null=True)
    languages = models.CharField(max_length=255,null=True)
    price_per_night = models.CharField(max_length=255,null=True)
    price_per_week = models.CharField(max_length=255,null=True)
    price_per_month = models.CharField(max_length=255,null=True)
    house_rules = models.CharField(max_length=255,null=True)
    photos = models.ImageField(upload_to='property/', null=True,blank=True)
    gstin = models.CharField(max_length=255,null=True)
    pan = models.CharField(max_length=255,null=True)
    aadhar = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    area=models.CharField(max_length=255,null=True)
    locationState=models.CharField(max_length=200,null=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f"{self.property_type} in {self.city}, {self.state}"









