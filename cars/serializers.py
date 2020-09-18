from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("owner", "make", "model", "doors", "price")
        model = Car