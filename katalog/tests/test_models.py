from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
    def setUp(self):
        CatalogItem.objects.create(item_name="Laptop", item_price=10000000, item_stock=1, description="Sebuah Laptop", rating=5, item_url="https://acer.com")

    def test_katalog_models(self):
        laptop = CatalogItem.objects.get(item_name="Laptop")
        self.assertEquals(laptop.item_name, "Laptop")