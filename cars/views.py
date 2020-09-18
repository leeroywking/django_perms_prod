# from django.shortcuts import render
# Create your views here.

from rest_framework import generics
from .models import Car
from .permissions import IsAuthorOrReadOnly
from .serializers import CarSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer