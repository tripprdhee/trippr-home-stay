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
    property_type = models.CharField(max_length=255,null=True,blank=True)
    number_properties = models.CharField(max_length=255,null=True,blank=True)
    property_model = models.CharField(max_length=255,null=True,blank=True)
    property_name = models.CharField(max_length=255,null=True,blank=True)
    house_number = models.CharField(max_length=255,null=True,blank=True)
    postal_code = models.CharField(max_length=10,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    landmark = models.CharField(max_length=255,null=True,blank=True)
    instructions = models.TextField(blank=True)
    number_of_bedrooms = models.CharField(max_length=255,blank=True)
    beds = models.CharField(max_length=255,blank=True)
    living_room = models.CharField(max_length=255,null=True,blank=True)
    other_spaces = models.CharField(max_length=255,null=True,blank=True)
    shared_spaces = models.CharField(max_length=255,null=True,blank=True)
    allowed_guest = models.CharField(max_length=255,null=True,blank=True)
    bathroom = models.CharField(max_length=255,null=True,blank=True)
    number_of_bathrooms = models.CharField(max_length=255,null=True,blank=True)
    no_of_separate_bathrooms = models.CharField(max_length=255,null=True,blank=True)
    apartment_size = models.CharField(max_length=255,null=True,blank=True)
    general_amenities = models.CharField(max_length=255,null=True,blank=True)
    cooking_cleaning_amenities = models.CharField(max_length=255,null=True,blank=True)
    other_amenities = models.CharField(max_length=255,null=True,blank=True)
    outside_view = models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=100,unique=True,null=True,blank=True)
    free_meals = models.CharField(max_length=255,null=True,blank=True)
    paid_meals = models.CharField(max_length=255,null=True,blank=True)
    parking = models.CharField(max_length=255,null=True,blank=True)
    parking_spots = models.CharField(max_length=255,null=True,blank=True)
    languages = models.CharField(max_length=255,null=True,blank=True)
    price_per_night = models.CharField(max_length=255,null=True,blank=True)
    price_per_week = models.CharField(max_length=255,null=True,blank=True)
    price_per_month = models.CharField(max_length=255,null=True,blank=True)
    house_rules = models.CharField(max_length=255,null=True,blank=True)
    photos = models.CharField(max_length=250, null=True,blank=True)
    bank_details=models.CharField(max_length=250,null=True,blank=True)
    gstin = models.CharField(max_length=255,null=True,blank=True)
    pan = models.CharField(max_length=255,null=True,blank=True)
    aadhar = models.CharField(max_length=255,null=True,blank=True)
    state = models.CharField(max_length=255,null=True,blank=True)
    area=models.CharField(max_length=255,null=True,blank=True)
    locationState=models.CharField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,)
    

    def __str__(self):
        return f"{self.property_type} in {self.city}, {self.state}"









