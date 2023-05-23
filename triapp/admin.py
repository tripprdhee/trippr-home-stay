from django.contrib import admin
from triapp.models import host_UserData,Property
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','username','email','phone','password','token']
class HostAdmin(admin.ModelAdmin):
    list_display = ['id', 'property_type', 'number_properties', 'property_model', 'property_name', 'house_number', 'postal_code', 'city', 'landmark', 'instructions', 'number_of_bedrooms', 'beds', 'living_room', 'other_spaces', 'shared_spaces', 'allowed_guest', 'bathroom', 'number_of_bathrooms', 'no_of_separate_bathrooms', 'apartment_size', 'general_amenities', 'cooking_cleaning_amenities', 'other_amenities', 'outside_view', 'meals_type', 'free_meals', 'paid_meals', 'parking', 'parking_spots', 'languages', 'price_per_night', 'price_per_week', 'price_per_month', 'house_rules', 'photos', 'gstin', 'pan', 'aadhar', 'state', 'is_active', 'is_deleted', 'created_at', 'updated_at']    
admin.site.register(host_UserData,EmployeeAdmin)
admin.site.register(Property,HostAdmin)
