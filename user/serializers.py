from rest_framework import serializers
from .models import brainjaiib

class jaiibserializer(serializers.ModelSerializer):
    class Meta:
        model=brainjaiib
        fields= '__all__'
