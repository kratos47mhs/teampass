from django.contrib import admin
from .models import (
    Api,
    AutomaticDel,
    Cache,
    CacheTree,
    Categories,
    CategoriesFolders,
    CategoriesItems,
    DefusePasswords,
    Emails,
    Export,
    Files,
    Items,
    ItemsChange,
    ItemsEdition,
    Kb,
    KbCategories,
    KbItems,
    Languages,
    LdapGroupsRoles,
    LogItems,
    LogSystem,
    Misc,
    NestedTree,
    Notification,
    Otv,
    Processes,
    ProcessesLogs,
    ProcessesTasks,
    RestrictionToRoles,
    Rights,
    RolesTitle,
    RolesValues,
    SharekeysFields,
    SharekeysFiles,
    SharekeysItems,
    SharekeysLogs,
    SharekeysSuggestions,
    Suggestion,
    Tags,
    Templates,
    Tokens,
    Users,
)

admin.site.register(Api)
admin.site.register(AutomaticDel)
admin.site.register(Cache)
admin.site.register(CacheTree)
admin.site.register(Categories)
admin.site.register(CategoriesFolders)
admin.site.register(CategoriesItems)
admin.site.register(DefusePasswords)
admin.site.register(Emails)
admin.site.register(Export)
admin.site.register(Files)
admin.site.register(Items)
admin.site.register(ItemsChange)
admin.site.register(ItemsEdition)
admin.site.register(Kb)
admin.site.register(KbCategories)
admin.site.register(KbItems)
admin.site.register(Languages)
admin.site.register(LdapGroupsRoles)
admin.site.register(LogItems)
admin.site.register(LogSystem)
admin.site.register(Misc)
admin.site.register(NestedTree)
admin.site.register(Notification)
admin.site.register(Otv)
admin.site.register(Processes)
admin.site.register(ProcessesLogs)
admin.site.register(ProcessesTasks)
admin.site.register(RestrictionToRoles)
admin.site.register(Rights)
admin.site.register(RolesTitle)
admin.site.register(RolesValues)
admin.site.register(SharekeysFields)
admin.site.register(SharekeysFiles)
admin.site.register(SharekeysItems)
admin.site.register(SharekeysLogs)
admin.site.register(SharekeysSuggestions)
admin.site.register(Suggestion)
admin.site.register(Tags)
admin.site.register(Templates)
admin.site.register(Tokens)
admin.site.register(Users)
