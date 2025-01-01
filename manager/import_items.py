# management/commands/import_items.py
from django.core.management.base import BaseCommand
from .models import Items
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('items.json') as f:
            data = json.load(f)
            for item in data:
                Items.objects.create(**item)