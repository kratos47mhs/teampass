# forms.py
from django import forms
from .models import Items


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ["label", "login", "password", "url", "description"]
