from django import forms
from django.contrib.auth.forms import UserCreationForm
from manager.models import Item, Folder, File, CustomUser


# Form for the Item model
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["description"]
        widgets = {
            "pw": forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(ItemForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["folder"].queryset = Folder.objects.filter(user=user)


# Custom user creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "login",
            "email",
            "name",
            "lastname",
        )


# Form for the Folder model
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["name", "item_id"]  # renamed from "item"


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = "__all__"
