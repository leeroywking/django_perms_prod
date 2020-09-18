from django.urls import path
from .views import CarList, CarDetail

urlpatterns = [path("<int:pk>/", CarDetail.as_view()), path("", CarList.as_view())]
