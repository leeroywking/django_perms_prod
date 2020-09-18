from django.test import TestCase
from django.contrib.auth.models import User

from .models import Car


class CarTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # Create a car
        test_car = Car.objects.create(
            owner="testuser1", make="Ford", model="Mustang", doors=3, price=800
        )
        testuser1.save()

    def test_car_content(self):
        car = Car.objects.get(id=1)
        actual_owner = f"{car.author}"
        actual_make = f"{car.title}"
        actual_model = f"{car.body}"
        self.assertEqual(actual_make, "Ford")
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_model, "Mustang")
