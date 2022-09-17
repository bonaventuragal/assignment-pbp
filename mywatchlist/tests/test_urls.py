from django.test import TestCase, Client
from django.urls import reverse, resolve
from mywatchlist.views import show_watchlist_html, show_watchlist_json, show_watchlist_xml

class TestUrls(TestCase):
    def test_html_url(self):
        client = Client()
        response = client.get(reverse("mywatchlist:watchlist_html"))
        self.assertEquals(response.status_code, 200)

    def test_json_url(self):
        client = Client()
        response = client.get(reverse("mywatchlist:watchlist_json"))
        self.assertEquals(response.status_code, 200)

    def test_xml_url(self):
        client = Client()
        response = client.get(reverse("mywatchlist:watchlist_xml"))
        self.assertEquals(response.status_code, 200)