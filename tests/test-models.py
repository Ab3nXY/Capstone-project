from django.test import TestCase
from restaurant.models import Menu  

class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu(title='Sample Item', price=12.99, inventory=50)
        expected_representation = 'Sample Item : $12.99'
        self.assertEqual(str(menu_item), expected_representation)
