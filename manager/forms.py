from django import forms
from django.contrib.auth.forms import UserCreationForm
from manager.models.models import Item, Folder, File
from manager.models.user import CustomUser


# Form for the Item model
class ItemForm(forms.ModelForm):
    pw = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Item
        fields = ["label", "pw", "url", "description", "folder"]

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
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["title", "parent"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(FolderForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["parent"].queryset = Folder.objects.filter(user=user)


# Form for the File model
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["name", "item"]

    def __init__(self, *args, **kwargs):
        item = kwargs.pop("item", None)
        super(FileForm, self).__init__(*args, **kwargs)
        if item:
            self.fields["item"].initial = item
            self.fields["item"].widget = forms.HiddenInput()
