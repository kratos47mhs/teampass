from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import jsonfield


class API(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)
    label = models.CharField(max_length=255, null=True)
    value = models.TextField(null=True)
    timestamp = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "api"


class DeletionConfiguration(models.Model):
    item = models.OneToOneField("Item", on_delete=models.CASCADE, primary_key=True)
    del_enabled = models.BooleanField()
    del_type = models.BooleanField()
    del_value = models.CharField(max_length=35)

    class Meta:
        db_table = "automatic_del"


class CacheEntry(models.Model):
    increment_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    label = models.CharField(max_length=500)
    description = models.TextField(null=True)
    tags = models.TextField(null=True)
    id_tree = models.IntegerField()
    perso = models.BooleanField()
    restricted_to = models.CharField(max_length=200, null=True)
    login = models.TextField(null=True)
    folder = models.TextField()
    author = models.CharField(max_length=50)
    renewal_period = models.SmallIntegerField(default=0)
    timestamp = models.CharField(max_length=50, null=True)
    url = models.TextField(null=True)
    encryption_type = models.CharField(max_length=50, default="0")

    class Meta:
        db_table = "cache"


class CacheTree(models.Model):
    increment_id = models.AutoField(primary_key=True)
    data = jsonfield.JSONField(null=True)
    visible_folders = models.TextField()
    timestamp = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folders = jsonfield.JSONField(null=True)

    class Meta:
        db_table = "cache_tree"


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


# Continue defining other models similarly...


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=500)
    description = models.TextField(null=True)
    pw = models.TextField(null=True)
    pw_iv = models.TextField(null=True)
    pw_len = models.IntegerField(default=0)
    url = models.TextField(null=True)
    id_tree = models.CharField(max_length=10, null=True)
    perso = models.BooleanField(default=False)
    login = models.CharField(max_length=200, null=True)
    inactif = models.BooleanField(default=False)
    restricted_to = models.CharField(max_length=200, null=True)
    anyone_can_modify = models.BooleanField(default=False)
    email = models.CharField(max_length=100, null=True)
    notification = models.CharField(max_length=250, null=True)
    viewed_no = models.IntegerField(default=0)
    complexity_level = models.CharField(max_length=3, default="-1")
    auto_update_pwd_frequency = models.SmallIntegerField(default=0)
    auto_update_pwd_next_date = models.CharField(max_length=100, default="0")
    encryption_type = models.CharField(max_length=20, default="not_set")
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE)
    fa_icon = models.CharField(max_length=100, null=True)
    item_key = models.CharField(max_length=500, default="-1")
    created_at = models.CharField(max_length=30, null=True)
    updated_at = models.CharField(max_length=30, null=True)
    deleted_at = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "items"


# Continuing from the previous models...


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
    file = models.CharField(max_length=50)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=50, default="none")

    class Meta:
        db_table = "items_change"


class ItemEdition(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    nleft = models.IntegerField(default=0)
    nright = models.IntegerField(default=0)
    nlevel = models.IntegerField(default=0)
    bloquer_creation = models.BooleanField(default=False)
    bloquer_modification = models.BooleanField(default=False)
    personal_folder = models.BooleanField(default=False)
    renewal_period = models.IntegerField(default=0)
    fa_icon = models.CharField(max_length=100, default="fas fa-folder")
    fa_icon_selected = models.CharField(max_length=100, default="fas fa-folder-open")
    categories = jsonfield.JSONField()
    nb_items_in_folder = models.IntegerField(default=0)
    nb_subfolders = models.IntegerField(default=0)
    nb_items_in_subfolders = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "nested_tree"


class Notification(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="notifications"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "notification"


class OTV(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    originator = models.ForeignKey(User, on_delete=models.CASCADE)
    encrypted = models.TextField()
    views = models.IntegerField(default=0)
    max_views = models.IntegerField(null=True)
    time_limit = models.CharField(max_length=100, null=True)
    shared_globaly = models.BooleanField(default=False)

    class Meta:
        db_table = "otv"


class Process(models.Model):
    increment_id = models.AutoField(primary_key=True)
    created_at = models.CharField(max_length=50)
    started_at = models.CharField(max_length=50, null=True)
    updated_at = models.CharField(max_length=50, null=True)
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
    created_at = models.CharField(max_length=20)
    job = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    updated_at = models.CharField(max_length=20, null=True)
    finished_at = models.CharField(max_length=20, null=True)
    treated_objects = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = "processes_logs"


class ProcessTask(models.Model):
    increment_id = models.AutoField(primary_key=True)
    process = models.ForeignKey(Process, on_delete=models.CASCADE)
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50, null=True)
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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_fields"


class ShareKeyFile(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_files"


class ShareKeyItem(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_items"


class ShareKeyLog(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_key = models.TextField()

    class Meta:
        db_table = "sharekeys_logs"


class ShareKeySuggestion(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object = models.ForeignKey("Suggestion", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)

    class Meta:
        db_table = "tokens"


class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=500, unique=True)
    pw = models.CharField(max_length=400)
    visible_groups = models.CharField(max_length=1000)
    last_items = models.TextField(null=True)
    key_tempo = models.CharField(max_length=100, null=True)
    last_pw_change = models.CharField(max_length=30, null=True)
    last_pw = models.TextField(null=True)
    admin = models.BooleanField(default=False)
    functions = models.CharField(max_length=1000, null=True)
    forbidden_groups = models.CharField(max_length=1000, null=True)
    last_connection = models.CharField(max_length=30, null=True)
    manager = models.IntegerField(default=0)
    email = models.CharField(max_length=300, default="none")
    favorites = models.CharField(max_length=1000, null=True)
    latest_items = models.CharField(max_length=1000, null=True)
    personal_folder = models.BooleanField(default=False)
    disabled = models.BooleanField(default=False)
    no_bad_attempts = models.BooleanField(default=False)
    can_create_root_folder = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    timestamp = models.CharField(max_length=30, default="0")
    language = models.CharField(max_length=50, default="0")
    name = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    session_end = models.CharField(max_length=30, null=True)
    is_administrated_by_role = models.BooleanField(default=False)
    psk = models.CharField(max_length=400, null=True)
    ga = models.CharField(max_length=50, null=True)
    ga_temporary_code = models.CharField(max_length=20, default="none")
    avatar = models.CharField(max_length=1000, null=True)
    avatar_thumb = models.CharField(max_length=1000, null=True)
    upgrade_needed = models.BooleanField(default=False)
    tree_load_strategy = models.CharField(max_length=30, default="full")
    can_manage_all_users = models.BooleanField(default=False)
    timezone = models.CharField(max_length=50, default="not_defined")
    agses_user_card_id = models.CharField(max_length=50, default="0")
    encrypted_psk = models.TextField(null=True)
    user_ip = models.CharField(max_length=400, default="none")
    user_ip_lastdate = models.CharField(max_length=50, null=True)
    yubico_user_key = models.CharField(max_length=100, default="none")
    yubico_user_id = models.CharField(max_length=100, default="none")
    public_key = models.TextField(null=True)
    private_key = models.TextField(null=True)
    special = models.CharField(max_length=250, default="none")
    auth_type = models.CharField(max_length=200, default="local")
    is_ready_for_usage = models.BooleanField(default=False)
    otp_provided = models.BooleanField(default=False)
    roles_from_ad_groups = models.CharField(max_length=1000, null=True)
    ongoing_process_id = models.CharField(max_length=100, null=True)
    mfa_enabled = models.BooleanField(default=True)
    created_at = models.CharField(max_length=30, null=True)
    updated_at = models.CharField(max_length=30, null=True)
    deleted_at = models.CharField(max_length=30, null=True)
    keys_recovery_time = models.CharField(max_length=500, null=True)
    aes_iv = models.TextField(null=True)

    class Meta:
        db_table = "users"
