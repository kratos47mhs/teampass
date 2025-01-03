from django.urls import path
from .views import FolderCreateView, FolderList

app_name = "manager"

urlpatterns = [
    path("folders/", FolderList.as_view(), name="folder_list"),
    path("new/", FolderCreateView.as_view(), name="folder_new"),
]