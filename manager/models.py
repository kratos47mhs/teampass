# teampass/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.timezone import now


class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"


class File(models.Model):
    name = models.CharField(max_length=255)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)


class Folder(models.Model):
    title = models.CharField(max_length=255)
    parent_folder_ptr = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        db_table = "folders"


class RoleTitle(models.Model):
    name = models.CharField(max_length=50)
    allow_pw_change = models.BooleanField(default=False)
    complexity = models.IntegerField(default=0)


class RoleValue(models.Model):
    role = models.ForeignKey(RoleTitle, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, default="R")


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=500, unique=True)
    pw = models.CharField(max_length=400)
    username = models.CharField(max_length=255, unique=True)
    groupes_visibles = models.TextField()
    derniers = models.TextField(null=True)
    key_tempo = models.CharField(max_length=100, null=True)
    last_pw_change = models.CharField(max_length=30, null=True)
    last_pw = models.TextField(null=True)
    admin = models.BooleanField(default=False)
    fonction_id = models.CharField(max_length=1000, null=True)
    groupes_interdits = models.CharField(max_length=1000, null=True)
    last_connexion = models.CharField(max_length=30, null=True)
    gestionnaire = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    favourites = models.TextField(null=True)
    latest_items = models.TextField(null=True)
    personal_folder = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    no_bad_attempts = models.BooleanField(default=False)
    can_create_root_folder = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    timestamp = models.CharField(max_length=30, null=True, default="0")
    user_language = models.CharField(max_length=50, null=True, default="0")
    name = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    session_end = models.CharField(max_length=30, null=True)
    isAdministratedByRole = models.BooleanField(default=False)
    psk = models.CharField(max_length=400, null=True)
    ga = models.CharField(max_length=50, null=True)
    ga_temporary_code = models.CharField(max_length=20, default="none")
    avatar = models.CharField(max_length=1000, null=True)
    avatar_thumb = models.CharField(max_length=1000, null=True)
    upgrade_needed = models.BooleanField(default=False)
    treeloadstrategy = models.CharField(max_length=30, null=True, default="full")
    can_manage_all_users = models.BooleanField(default=False)
    usertimezone = models.CharField(max_length=50, null=True, default="not_defined")
    agses_usercardid = models.CharField(max_length=50, null=True, default="0")

    class Meta:
        db_table = "customusers"


class CustomPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)

    class Meta:
        db_table = "custom_permissions"


# Restricting permissions to roles
class RoleTitle(models.Model):
    name = models.CharField(max_length=50)
    allow_pw_change = models.BooleanField(default=False)
    complexity = models.IntegerField(default=0)


# Define a Role model
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    permissions = models.ManyToManyField("Permission")


# Define a Permission model
class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()


# Define a Token model
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="tokens"
    )
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)


# Define a Suggestion model
class Suggestion(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    pw = models.TextField()
    pw_iv = models.TextField()
    pw_len = models.IntegerField()
    description = models.TextField()
    author_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="suggestions"
    )
    folder_id = models.IntegerField()
    comment = models.TextField()
    suggestion_type = models.CharField(max_length=10, default="new")
    encryption_type = models.CharField(max_length=20, default="not_set")


# Define a SharekeysItem model
class SharekeysItem(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="shared_items"
    )
    share_key = models.TextField()


# Define a SharekeysLog model
class SharekeysLog(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="share_logs"
    )
    share_key = models.TextField()


# Define a SharekeysSuggestion model
class SharekeysSuggestion(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="suggestions_shared"
    )
    share_key = models.TextField()


# Define a Tag model
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    item_id = models.IntegerField()


# Define a Template model
class Template(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    category_id = models.IntegerField()


# Define a UsersTable (renamed from IppassUsers) to avoid conflicts
class UsersTable(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=500, unique=True)
    pw = models.CharField(max_length=400)
    groupes_visibles = models.TextField()
    derniers = models.TextField(null=True)
    key_tempo = models.CharField(max_length=100, null=True)
    last_pw_change = models.CharField(max_length=30, null=True)
    last_pw = models.TextField(null=True)
    admin = models.BooleanField(default=False)
    fonction_id = models.CharField(max_length=1000, null=True)
    groupes_interdits = models.CharField(max_length=1000, null=True)
    last_connexion = models.CharField(max_length=30, null=True)
    gestionnaire = models.IntegerField(default=0)
    email = models.EmailField(null=True, default="none")
    favourites = models.TextField(null=True)
    latest_items = models.TextField(null=True)
    personal_folder = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    no_bad_attempts = models.BooleanField(default=False)
    can_create_root_folder = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    timestamp = models.CharField(max_length=30, null=True, default="0")
    user_language = models.CharField(max_length=50, null=True, default="0")
    name = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    session_end = models.CharField(max_length=30, null=True)
    isAdministratedByRole = models.BooleanField(default=False)
    psk = models.CharField(max_length=400, null=True)
    ga = models.CharField(max_length=50, null=True)
    ga_temporary_code = models.CharField(max_length=20, default="none")
    avatar = models.CharField(max_length=1000, null=True)
    avatar_thumb = models.CharField(max_length=1000, null=True)
    upgrade_needed = models.BooleanField(default=False)
    treeloadstrategy = models.CharField(max_length=30, null=True, default="full")
    can_manage_all_users = models.BooleanField(default=False)
    usertimezone = models.CharField(max_length=50, null=True, default="not_defined")
    agses_usercardid = models.CharField(max_length=50, null=True, default="0")


# Define a Token model (renamed from Token) to avoid conflicts
class Tokens(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="tokens"
    )
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)


# Define a Token model (renamed from Tokens) to avoid conflicts
class Token(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_tokens"
    )
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)


# Define a Token model (renamed from Tokens) to avoid conflicts
class UserTokens(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_tokens"
    )
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)


# Define a Template model (renamed from Template) to avoid conflicts
class UserTemplates(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    category_id = models.IntegerField()


# Define a Tag model (renamed from Tag) to avoid conflicts
class UserTags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    item_id = models.IntegerField()


# Define a Template model (renamed from Template) to avoid conflicts
class UserTemplates(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    category_id = models.IntegerField()


# Define a Role model (renamed from Role) to avoid conflicts
class UserRoles(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_roles"
    )
    role_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)


# Define a Permission model (renamed from Permission) to avoid conflicts
class UserPermissions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_permissions"
    )
    permission_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)


# Define a Suggestion model (renamed from Suggestion) to avoid conflicts
class UserSuggestions(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_suggestions"
    )
    suggestion_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)


# Define a SharekeysItem model (renamed from SharekeysItem) to avoid conflicts
class UserSharedItems(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_shared_items"
    )
    share_key = models.TextField()


# Define a SharekeysLog model (renamed from SharekeysLog) to avoid conflicts
class UserShareLogs(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_share_logs"
    )
    share_key = models.TextField()


# Define a SharekeysSuggestion model (renamed from SharekeysSuggestion) to avoid conflicts
class UserSuggestionsShared(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        UsersTable, on_delete=models.CASCADE, related_name="user_suggestions_shared"
    )
    share_key = models.TextField()


# Define a Tag model (renamed from Tag) to avoid conflicts
class UserTags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    item_id = models.IntegerField()


# Define a Token model (renamed from Tokens) to replace Django's built-in token system
class CustomToken(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="tokens"
    )
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)


# Define a Role model (renamed from UserRoles) to replace Django's built-in role system
class CustomRole(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_roles"
    )
    role_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)


# Define a Permission model (renamed from UserPermissions) to replace Django's built-in permission system
class CustomPermission(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_permissions"
    )
    permission_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)


# Define a Suggestion model (renamed from UserSuggestions) to replace Django's built-in suggestion system
class CustomSuggestion(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_suggestions"
    )
    suggestion_id = models.IntegerField()
    creation_timestamp = models.CharField(max_length=50)


# Define a SharekeysItem model (renamed from UserSharedItems) to replace Django's built-in share keys system
class CustomShareKeys(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_shared_items"
    )
    share_key = models.TextField()


# Define a SharekeysLog model (renamed from UserShareLogs) to replace Django's built-in share keys log system
class CustomShareLogs(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_share_logs"
    )
    share_key = models.TextField()


# Define a SharekeysSuggestion model (renamed from UserSuggestionsShared) to replace Django's built-in suggestion system
class CustomSuggestionsShared(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_suggestions_shared"
    )
    share_key = models.TextField()


# Define a Tag model (renamed from UserTags) to replace Django's built-in tag system
class CustomTag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    item_id = models.IntegerField()
    # Add any additional fields specific to your user model


class ShareKeyField(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="share_key_fields"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()


class Token(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    class Meta:
        db_table = "tokens"


# Use Django's built-in ORM for the following models
class OTV(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    originator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=100)


class Process(models.Model):
    process_id = models.IntegerField(null=True)
    started_at = models.CharField(max_length=50, null=True)
    finished_at = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"Process {self.process_id}"


class Notification(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class ProcessLog(models.Model):
    job = models.CharField(max_length=50)
    status = models.CharField(max_length=10)


# Use Django's built-in ORM for the following models
class ProcessTask(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task {self.process_id}"


class RestrictionToRole(models.Model):
    role = models.ForeignKey(RoleTitle, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class ShareKeyFile(models.Model):
    object = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return f"Share key file for {self.object}"


# Use Django's built-in ORM for the following models
class SystemLog(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    date = models.DateTimeField()


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"


# manager.NestedFolder model
class NestedFolder(models.Model):
    parent = models.ForeignKey(Folder, on_delete=models.CASCADE)

class RoleTitle(models.Model):
    name = models.CharField(max_length=50)
    allow_pw_change = models.BooleanField(default=False)
    complexity = models.IntegerField(default=0)


class RoleValue(models.Model):
    role = models.ForeignKey(RoleTitle, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, default="R")


class ShareKeyField(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="share_key_fields"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()


class Token(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    class Meta:
        db_table = "tokens"


# Use Django's built-in ORM for the following models
class OTV(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    originator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=100)


class Process(models.Model):
    process_id = models.IntegerField(null=True)
    started_at = models.CharField(max_length=50, null=True)
    finished_at = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"Process {self.process_id}"


class Notification(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class ProcessLog(models.Model):
    job = models.CharField(max_length=50)
    status = models.CharField(max_length=10)


# Use Django's built-in ORM for the following models
class ProcessTask(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task {self.process_id}"


class RestrictionToRole(models.Model):
    role = models.ForeignKey(RoleTitle, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class ShareKeyFile(models.Model):
    object = models.ForeignKey("File", on_delete=models.CASCADE)

    def __str__(self):
        return f"Share key file for {self.object}"
