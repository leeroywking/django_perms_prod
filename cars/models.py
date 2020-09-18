from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.TextField()
    model = models.TextField()
    doors = models.IntegerField(
        choices=[(2, "Coup"), (3, "hatchback"), (4, "sedan"), (5, "station wagon")]
    )
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model
