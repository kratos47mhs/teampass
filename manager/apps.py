from django.apps import AppConfig


class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager'

    def ready(self):
        # Update the database schema here
        import manager.models as models
        from manager.models import Item, CustomUser, Folder, File