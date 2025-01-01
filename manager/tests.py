# tests.py
from django.test import TestCase
from .models import Item

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(label='Test Item', login='test', password='password', url='http://example.com')

    def test_item_creation(self):
        item = Item.objects.get(label='Test Item')
        self.assertEqual(item.login, 'test')