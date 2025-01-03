"""
URL configuration for teampass project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from manager import views

urlpatterns = [
    # Admin URLs
    path("admin/", admin.site.urls),
    # Authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    # App-specific URLs
    path("", views.home, name="home"),
    path("item/", views.item_list, name="item_list"),
    path("item/<int:pk>/", views.item_detail, name="item_detail"),
    path("item/new/", views.item_create, name="item_create"),
    path("item/<int:pk>/edit/", views.item_update, name="item_update"),
    path("item/<int:pk>/delete/", views.item_delete, name="item_delete"),
    # Folder URLs
    path("folders/", views.folder_list, name="folder_list"),
    path("folders/<int:pk>/", views.folder_detail, name="folder_detail"),
    path("folders/new/", views.folder_create, name="folder_create"),
    path("folders/<int:pk>/edit/", views.folder_update, name="folder_update"),
    path("folders/<int:pk>/delete/", views.folder_delete, name="folder_delete"),
    # User URLs
    path("register/", views.user_register, name="user_register"),
    path("profile/", views.user_profile, name="user_profile"),
    path("users/", views.user_list, name="user_list"),
    path("users/<int:pk>/", views.user_detail, name="user_detail"),
    path("users/new/", views.user_create, name="user_create"),
    path("users/<int:pk>/edit/", views.user_update, name="user_update"),
    path("users/<int:pk>/delete/", views.user_delete, name="user_delete"),
    path("users/<int:pk>/edit/", views.user_update, name="user_update"),
    # API URLs
    path("api/", include("manager.api.urls")),  # Assuming you have an API app
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
