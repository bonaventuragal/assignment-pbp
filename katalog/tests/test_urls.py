from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_catalog

class TestUrls(TestCase):
    def test_katalog_urls(self):
        url = reverse("katalog:katalog")
        self.assertEquals(resolve(url).func, show_catalog)