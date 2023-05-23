from rest_framework import serializers
from .models import host_UserData, Property

class host_UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = host_UserData
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
