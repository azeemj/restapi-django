from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient

from .views import detail, inventory


class URLTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_urls(self):
        """
        Ensure API works.
        """
        url = 'http://localhost:8000/api/inventory/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_urls_inventory_list(self):
        found = resolve('/frontapp/inventory-list')
        self.assertEqual(found.func, inventory)

    def test_urls_details(self):
        found = resolve('/frontapp/details/2')
        self.assertEqual(found.func, detail)