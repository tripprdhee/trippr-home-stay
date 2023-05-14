from django.contrib import admin
from triapp.models import host_UserData,Property
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','username','email','phone','password']
class HostAdmin(admin.ModelAdmin):
    list_display=['id','type','rental_mode','area','city','state','pincode','description','sleeping_arrangement','washrooms','images','nearest_station_airport','nearest_station_bus','nearest_station_train','photos','amenities','preferred_guest','length_of_stay',]
    
admin.site.register(host_UserData,EmployeeAdmin)
admin.site.register(Property,HostAdmin)
