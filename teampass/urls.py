from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from manage import views


urlpatterns = [
    # Admin URLs
    path("admin/", admin.site.urls),
    # Authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    # App-specific URLs
    path("", views.home, name="home"),
    path("item/", include("manager.urls")),
    # API URLs
    path("api/", include("manager.api.urls")),  # Assuming you have an API app
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
