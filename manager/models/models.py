from django.utils.timezone import now
from django.db import models

# from django.core.files import File
from manager.models.user import CustomUser

import jsonfield


class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, default=1
    )  # Assuming 1 is a valid user ID
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = "folders"
        verbose_name = "Folder"
        verbose_name_plural = "Folders"

    def __str__(self):
        return self.title


class API(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)
    label = models.CharField(max_length=255, null=True)
    value = models.TextField(null=True)
    timestamp = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "api"


class DeletionConfiguration(models.Model):
    item = models.OneToOneField("Item", on_delete=models.CASCADE, primary_key=True)
    del_enabled = models.BooleanField()
    del_type = models.BooleanField()
    del_value = models.CharField(max_length=35)

    class Meta:
        db_table = "automatic_del"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    level = models.IntegerField()
    description = models.TextField(null=True)
    type = models.CharField(max_length=50, blank=True)
    masked = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    encrypted_data = models.BooleanField(default=True)
    role_visibility = models.CharField(max_length=255, default="all")
    is_mandatory = models.BooleanField(default=False)
    regex = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "categories"


class CategoryFolder(models.Model):
    increment_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE)

    class Meta:
        db_table = "categories_folders"


class CategoryItem(models.Model):
    id = models.AutoField(primary_key=True)
    field_id = models.IntegerField()
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    data = models.TextField()
    data_iv = models.TextField()
    encryption_type = models.CharField(max_length=20, default="not_set")
    is_mandatory = models.BooleanField(default=False)

    class Meta:
        db_table = "categories_items"


class Password(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    encrypted_password = models.TextField()
    password_iv = models.TextField()
    encryption_type = models.CharField(max_length=50, default="AES")
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="passwords"
    )
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "passwords"
        verbose_name = "Password"
        verbose_name_plural = "Passwords"

    def __str__(self):
        return self.label


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    encrypted_password = models.TextField(default="default_encrypted_password")
    password_iv = models.TextField(default="default_password_iv")
    encryption_type = models.CharField(max_length=50, default="AES")
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="item", default=1)  # Assuming 1 is a valid user ID
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "items"
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.label


class DefusePassword(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    object = models.ForeignKey("Item", on_delete=models.CASCADE)
    password = models.TextField()

    class Meta:
        db_table = "defuse_passwords"


class Email(models.Model):
    increment_id = models.AutoField(primary_key=True)
    timestamp = models.IntegerField()
    subject = models.TextField()
    body = models.TextField()
    receivers = models.TextField()
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "emails"


class Export(models.Model):
    increment_id = models.AutoField(primary_key=True)
    export_tag = models.CharField(max_length=20)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    label = models.CharField(max_length=500)
    login = models.CharField(max_length=100)
    description = models.TextField()
    pw = models.TextField()
    path = models.CharField(max_length=500)
    email = models.CharField(max_length=500, default="none")
    url = models.CharField(max_length=500, default="none")
    kbs = models.CharField(max_length=500, default="none")
    tags = models.CharField(max_length=500, default="none")
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE)
    perso = models.BooleanField(default=False)
    restricted_to = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "export"


class File(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    name = models.TextField()
    size = models.IntegerField()
    extension = models.CharField(max_length=10)
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="0")
    content = models.BinaryField(null=True)
    confirmed = models.IntegerField(default=0)

    class Meta:
        db_table = "files"


class ItemChange(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    label = models.CharField(max_length=255, default="none")
    pw = models.TextField()
    login = models.CharField(max_length=255, default="none")
    email = models.CharField(max_length=255, default="none")
    url = models.CharField(max_length=255, default="none")
    description = models.TextField()
    comment = models.TextField()
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=50, default="none")

    class Meta:
        db_table = "items_change"


class ItemEdition(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=50)

    class Meta:
        db_table = "items_edition"


class KBCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)

    class Meta:
        db_table = "kb_categories"


class KB(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(KBCategory, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    anyone_can_modify = models.BooleanField(default=False)

    class Meta:
        db_table = "kb"


class KBItem(models.Model):
    increment_id = models.AutoField(primary_key=True)
    kb = models.ForeignKey(KB, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)

    class Meta:
        db_table = "kb_items"


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    flag = models.CharField(max_length=50)
    code_poeditor = models.CharField(max_length=30)

    class Meta:
        db_table = "languages"


class LDAPGroupRole(models.Model):
    increment_id = models.AutoField(primary_key=True)
    role = models.ForeignKey("RoleTitle", on_delete=models.CASCADE)
    ldap_group_id = models.IntegerField()
    ldap_group_label = models.CharField(max_length=255)

    class Meta:
        db_table = "ldap_groups_roles"


class ItemLog(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=250, null=True)
    reason = models.TextField(null=True)
    old_value = models.TextField(null=True)
    encryption_type = models.CharField(max_length=20, default="not_set")

    class Meta:
        db_table = "log_items"


class SystemLog(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    date = models.CharField(max_length=30)
    label = models.TextField()
    user = models.CharField(max_length=255)
    field_1 = models.CharField(max_length=250, null=True)

    class Meta:
        db_table = "log_system"


class Misc(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    intitule = models.CharField(max_length=100)
    valeur = models.CharField(max_length=500)

    class Meta:
        db_table = "misc"


class Notification(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="notifications"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "notification"


class OTV(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    originator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    encrypted = models.TextField()
    views = models.IntegerField(default=0)
    max_views = models.IntegerField(null=True)
    time_limit = models.CharField(max_length=100, null=True)
    shared_globaly = models.BooleanField(default=False)

    class Meta:
        db_table = "otv"


class Process(models.Model):
    increment_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
    started_at = models.CharField(max_length=50, null=True)
    finished_at = models.CharField(max_length=50, null=True)
    process_id = models.IntegerField(null=True)
    process_type = models.CharField(max_length=100)
    output = models.TextField(null=True)
    arguments = jsonfield.JSONField()
    is_in_progress = models.BooleanField(default=False)
    item = models.ForeignKey("Item", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "processes"


class ProcessLog(models.Model):
    increment_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
    job = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    finished_at = models.CharField(max_length=20, null=True)
    treated_objects = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "processes_logs"


class ProcessTask(models.Model):
    increment_id = models.AutoField(primary_key=True)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
    finished_at = models.CharField(max_length=50, null=True)
    task = jsonfield.JSONField()
    system_process_id = models.IntegerField(null=True)
    is_in_progress = models.BooleanField(default=False)
    sub_task_in_progress = models.BooleanField(default=False)

    class Meta:
        db_table = "processes_tasks"


class RestrictionToRole(models.Model):
    increment_id = models.AutoField(primary_key=True)
    role = models.ForeignKey("RoleTitle", on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)

    class Meta:
        db_table = "restriction_to_roles"


class Right(models.Model):
    id = models.AutoField(primary_key=True)
    tree = models.ForeignKey(Folder, on_delete=models.CASCADE)
    function = models.ForeignKey("RoleTitle", on_delete=models.CASCADE)
    authorized = models.BooleanField(default=False)

    class Meta:
        db_table = "rights"


class RoleTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    allow_pw_change = models.BooleanField(default=False)
    complexity = models.IntegerField(default=0)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = "roles_title"


class RoleValue(models.Model):
    increment_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(RoleTitle, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, default="R")

    class Meta:
        db_table = "roles_values"


class ShareKeyField(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="share_key_fields"
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_fields"


class ShareKeyFile(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_files"


class ShareKeyItem(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_items"


class ShareKeyLog(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_logs"


class ShareKeySuggestion(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey("Suggestion", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_suggestions"


class Suggestion(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    pw = models.TextField()
    pw_iv = models.TextField()
    pw_len = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    comment = models.TextField()
    suggestion_type = models.CharField(max_length=10, default="new")
    encryption_type = models.CharField(max_length=20, default="not_set")

    class Meta:
        db_table = "suggestion"


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=30)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)

    class Meta:
        db_table = "tags"


class Template(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "templates"


class Token(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)

    class Meta:
        db_table = "tokens"
