from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.all().delete()
        # Add test instances of the Menu model
        Menu.objects.create(id=4, title='Item 1', price=10.99, inventory=20)
        Menu.objects.create(id=5, title='Item 2', price=15.99, inventory=15)
        Menu.objects.create(id=6, title='Item 3', price=8.99, inventory=25)

    def test_getall(self):
        client = APIClient()

        # Retrieve all Menu objects using the API endpoint
        response = client.get('/restaurant/menu/')  # Replace '/menu/' with your actual API endpoint

        # Serialize the expected data from the test instances
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data in the response equals the expected data
        self.assertEqual(response.data, expected_data)
