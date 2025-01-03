from django.contrib import admin
from manager.models import (

    Category,
    File,
    Item,
    SystemLog,
    Folder,
    Notification,
    OTV,
    Process,
    ProcessLog,
    ProcessTask,
    RestrictionToRole,
    RoleTitle,
    RoleValue,
    ShareKeyField,
    ShareKeyFile,
    Suggestion,
    CustomUser,
    Tag,
    Template,
    Token,
)

# Register models with default admin options

admin.site.register(Category)
admin.site.register(File)
admin.site.register(Item)
admin.site.register(SystemLog)
admin.site.register(Folder)
admin.site.register(Notification)
admin.site.register(OTV)
admin.site.register(Process)
admin.site.register(ProcessLog)
admin.site.register(ProcessTask)
admin.site.register(RestrictionToRole)
admin.site.register(RoleTitle)
admin.site.register(RoleValue)
admin.site.register(ShareKeyField)
admin.site.register(ShareKeyFile)
admin.site.register(Suggestion)
admin.site.register(Tag)
admin.site.register(Template)
admin.site.register(Token)
admin.site.register(CustomUser)

# Create custom admin classes if needed

# Example: Custom admin for Item model
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'label', 'created_at', 'updated_at', 'deleted_at')
#     search_fields = ('label', 'description')
#     list_filter = ('perso', 'inactif', 'deleted_at')
#     raw_id_fields = ('id_tree', 'folder')  # Assuming folder is a ForeignKey

# Example: Custom admin for CustomUser model
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'login', 'email', 'admin', 'disabled')
#     search_fields = ('login', 'email')
#     list_filter = ('admin', 'disabled', 'is_ready_for_usage')
#     raw_id_fields = ('functions', 'forbidden_groups')  # Assuming these are ForeignKeys

# Add custom admin classes for other models as needed
