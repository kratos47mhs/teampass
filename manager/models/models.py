# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Folder(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )


class Item(models.Model):
    folder = TreeForeignKey(Folder, on_delete=models.CASCADE)
    # permission fields


class Api(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=15)
    label = models.CharField(max_length=255, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    timestamp = models.CharField(max_length=50)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "api"


class AutomaticDel(models.Model):
    item_id = models.IntegerField(primary_key=True)
    del_enabled = models.IntegerField()
    del_type = models.IntegerField()
    del_value = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = "automatic_del"


class Cache(models.Model):
    increment_id = models.AutoField(primary_key=True)
    id = models.IntegerField()
    label = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    id_tree = models.IntegerField()
    perso = models.IntegerField()
    restricted_to = models.CharField(max_length=200, blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    folder = models.TextField()
    author = models.CharField(max_length=50)
    renewal_period = models.IntegerField()
    timestamp = models.CharField(max_length=50, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    encryption_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cache"


class CacheTree(models.Model):
    increment_id = models.SmallAutoField(primary_key=True)
    data = models.JSONField(blank=True, null=True)
    visible_folders = models.TextField()
    timestamp = models.CharField(max_length=50)
    user_id = models.IntegerField()
    folders = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cache_tree"


class Categories(models.Model):
    parent_id = models.IntegerField()
    title = models.CharField(max_length=255)
    level = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    masked = models.IntegerField()
    order = models.IntegerField()
    encrypted_data = models.IntegerField()
    role_visibility = models.CharField(max_length=255)
    is_mandatory = models.IntegerField()
    regex = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "categories"


class CategoriesFolders(models.Model):
    increment_id = models.AutoField(primary_key=True)
    id_category = models.IntegerField()
    id_folder = models.IntegerField()

    class Meta:
        managed = False
        db_table = "categories_folders"


class CategoriesItems(models.Model):
    field_id = models.IntegerField()
    item_id = models.IntegerField()
    data = models.TextField()
    data_iv = models.TextField()
    encryption_type = models.CharField(max_length=20)
    is_mandatory = models.IntegerField()

    class Meta:
        managed = False
        db_table = "categories_items"


class DefusePasswords(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    object_id = models.IntegerField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = "defuse_passwords"


class Emails(models.Model):
    increment_id = models.AutoField(primary_key=True)
    timestamp = models.IntegerField()
    subject = models.TextField()
    body = models.TextField()
    receivers = models.TextField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "emails"


class Export(models.Model):
    increment_id = models.AutoField(primary_key=True)
    export_tag = models.CharField(max_length=20)
    item_id = models.IntegerField()
    label = models.CharField(max_length=500)
    login = models.CharField(max_length=100)
    description = models.TextField()
    pw = models.TextField()
    path = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    kbs = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    folder_id = models.CharField(max_length=10)
    perso = models.IntegerField()
    restricted_to = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "export"


class Files(models.Model):
    id_item = models.IntegerField()
    name = models.TextField()
    size = models.IntegerField()
    extension = models.CharField(max_length=10)
    type = models.CharField(max_length=255)
    file = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    confirmed = models.IntegerField()

    class Meta:
        managed = False
        db_table = "files"


class Items(models.Model):
    label = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    pw = models.TextField(blank=True, null=True)
    pw_iv = models.TextField(blank=True, null=True)
    pw_len = models.IntegerField()
    url = models.TextField(blank=True, null=True)
    id_tree = models.CharField(max_length=10, blank=True, null=True)
    perso = models.IntegerField()
    login = models.CharField(max_length=200, blank=True, null=True)
    inactif = models.IntegerField()
    restricted_to = models.CharField(max_length=200, blank=True, null=True)
    anyone_can_modify = models.IntegerField()
    email = models.CharField(max_length=100, blank=True, null=True)
    notification = models.CharField(max_length=250, blank=True, null=True)
    viewed_no = models.IntegerField()
    complexity_level = models.CharField(max_length=3)
    auto_update_pwd_frequency = models.IntegerField()
    auto_update_pwd_next_date = models.CharField(max_length=100)
    encryption_type = models.CharField(max_length=20)
    fa_icon = models.CharField(max_length=100, blank=True, null=True)
    item_key = models.CharField(max_length=500)
    created_at = models.CharField(max_length=30, blank=True, null=True)
    updated_at = models.CharField(max_length=30, blank=True, null=True)
    deleted_at = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "items"


class ItemsChange(models.Model):
    item_id = models.IntegerField()
    label = models.CharField(max_length=255)
    pw = models.TextField()
    login = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()
    comment = models.TextField()
    folder_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "items_change"


class ItemsEdition(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    timestamp = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "items_edition"


class Kb(models.Model):
    category_id = models.IntegerField()
    label = models.CharField(max_length=200)
    description = models.TextField()
    author_id = models.IntegerField()
    anyone_can_modify = models.IntegerField()

    class Meta:
        managed = False
        db_table = "kb"


class KbCategories(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "kb_categories"


class KbItems(models.Model):
    increment_id = models.AutoField(primary_key=True)
    kb_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "kb_items"


class Languages(models.Model):
    name = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    flag = models.CharField(max_length=50)
    code_poeditor = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = "languages"


class LdapGroupsRoles(models.Model):
    increment_id = models.AutoField(primary_key=True)
    role_id = models.IntegerField()
    ldap_group_id = models.IntegerField()
    ldap_group_label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "ldap_groups_roles"


class LogItems(models.Model):
    increment_id = models.AutoField(primary_key=True)
    id_item = models.IntegerField()
    date = models.CharField(max_length=50)
    id_user = models.IntegerField()
    action = models.CharField(max_length=250, blank=True, null=True)
    raison = models.TextField(blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    encryption_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "log_items"


class LogSystem(models.Model):
    type = models.CharField(max_length=20)
    date = models.CharField(max_length=30)
    label = models.TextField()
    qui = models.CharField(max_length=255)
    field_1 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "log_system"


class Misc(models.Model):
    increment_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    intitule = models.CharField(max_length=100)
    valeur = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = "misc"


class NestedTree(models.Model):
    id = models.BigAutoField(primary_key=True)
    parent_id = models.IntegerField()
    title = models.CharField(max_length=255)
    nleft = models.IntegerField()
    nright = models.IntegerField()
    nlevel = models.IntegerField()
    bloquer_creation = models.IntegerField()
    bloquer_modification = models.IntegerField()
    personal_folder = models.IntegerField()
    renewal_period = models.IntegerField()
    fa_icon = models.CharField(max_length=100)
    fa_icon_selected = models.CharField(max_length=100)
    categories = models.TextField()
    nb_items_in_folder = models.IntegerField()
    nb_subfolders = models.IntegerField()
    nb_items_in_subfolders = models.IntegerField()

    class Meta:
        managed = False
        db_table = "nested_tree"


class Notification(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "notification"


class Otv(models.Model):
    timestamp = models.TextField()
    code = models.CharField(max_length=100)
    item_id = models.IntegerField()
    originator = models.IntegerField()
    encrypted = models.TextField()
    views = models.IntegerField()
    max_views = models.IntegerField(blank=True, null=True)
    time_limit = models.CharField(max_length=100, blank=True, null=True)
    shared_globaly = models.IntegerField()

    class Meta:
        managed = False
        db_table = "otv"


class Processes(models.Model):
    increment_id = models.AutoField(primary_key=True)
    created_at = models.CharField(max_length=50)
    started_at = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.CharField(max_length=50, blank=True, null=True)
    finished_at = models.CharField(max_length=50, blank=True, null=True)
    process_id = models.IntegerField(blank=True, null=True)
    process_type = models.CharField(max_length=100)
    output = models.TextField(blank=True, null=True)
    arguments = models.JSONField()
    is_in_progress = models.IntegerField()
    item_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "processes"


class ProcessesLogs(models.Model):
    increment_id = models.AutoField(primary_key=True)
    created_at = models.CharField(max_length=20)
    job = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    updated_at = models.CharField(max_length=20, blank=True, null=True)
    finished_at = models.CharField(max_length=20, blank=True, null=True)
    treated_objects = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "processes_logs"


class ProcessesTasks(models.Model):
    increment_id = models.AutoField(primary_key=True)
    process_id = models.IntegerField()
    created_at = models.CharField(max_length=50)
    updated_at = models.CharField(max_length=50, blank=True, null=True)
    finished_at = models.CharField(max_length=50, blank=True, null=True)
    task = models.JSONField()
    system_process_id = models.IntegerField(blank=True, null=True)
    is_in_progress = models.IntegerField()
    sub_task_in_progress = models.IntegerField()

    class Meta:
        managed = False
        db_table = "processes_tasks"


class RestrictionToRoles(models.Model):
    increment_id = models.AutoField(primary_key=True)
    role_id = models.IntegerField()
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "restriction_to_roles"


class Rights(models.Model):
    tree_id = models.IntegerField()
    fonction_id = models.IntegerField()
    authorized = models.IntegerField()

    class Meta:
        managed = False
        db_table = "rights"


class RolesTitle(models.Model):
    title = models.CharField(max_length=50)
    allow_pw_change = models.IntegerField()
    complexity = models.IntegerField()
    creator_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "roles_title"


class RolesValues(models.Model):
    increment_id = models.AutoField(primary_key=True)
    role_id = models.IntegerField()
    folder_id = models.IntegerField()
    type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = "roles_values"


class SharekeysFields(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.IntegerField()
    share_key = models.TextField()

    class Meta:
        managed = False
        db_table = "sharekeys_fields"


class SharekeysFiles(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.IntegerField()
    share_key = models.TextField()

    class Meta:
        managed = False
        db_table = "sharekeys_files"


class SharekeysItems(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.IntegerField()
    share_key = models.TextField()

    class Meta:
        managed = False
        db_table = "sharekeys_items"


class SharekeysLogs(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.IntegerField()
    share_key = models.TextField()

    class Meta:
        managed = False
        db_table = "sharekeys_logs"


class SharekeysSuggestions(models.Model):
    increment_id = models.AutoField(primary_key=True)
    object_id = models.IntegerField()
    user_id = models.IntegerField()
    share_key = models.TextField()

    class Meta:
        managed = False
        db_table = "sharekeys_suggestions"


class Suggestion(models.Model):
    label = models.CharField(max_length=255)
    pw = models.TextField()
    pw_iv = models.TextField()
    pw_len = models.IntegerField()
    description = models.TextField()
    author_id = models.IntegerField()
    folder_id = models.IntegerField()
    comment = models.TextField()
    suggestion_type = models.CharField(max_length=10)
    encryption_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "suggestion"


class Tags(models.Model):
    tag = models.CharField(max_length=30)
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "tags"


class Templates(models.Model):
    increment_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "templates"


class Tokens(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    creation_timestamp = models.CharField(max_length=50)
    end_timestamp = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "tokens"



class User(models.Model):
    login = models.CharField(unique=True, max_length=500)
    password = models.CharField(max_length=400)  # Renamed from 'pw' for clarity
    visible_groups = models.CharField(max_length=1000)
    derniers = models.TextField(blank=True, null=True)
    tempo_key = models.CharField(max_length=100, blank=True, null=True)
    last_password_change = models.CharField(max_length=30, blank=True, null=True)
    last_password = models.TextField(blank=True, null=True)
    is_admin = models.IntegerField()
    fonction_id = models.CharField(max_length=1000, blank=True, null=True)
    forbidden_groups = models.CharField(max_length=1000, blank=True, null=True)
    last_connection = models.CharField(max_length=30, blank=True, null=True)
    user_manager = models.IntegerField()
    email = models.EmailField()  # Changed to EmailField for validation
    favorites = models.CharField(max_length=1000, blank=True, null=True)
    latest_items = models.CharField(max_length=1000, blank=True, null=True)
    personal_folder = models.IntegerField()
    is_disabled = models.BooleanField(default=False)  # Renamed and made BooleanField
    no_bad_attempts = models.IntegerField()
    can_create_root_folder = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)
    timestamp = models.DateTimeField()  # Changed to DateTimeField for better data type handling
    user_language = models.CharField(max_length=50)
    name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    session_end = models.CharField(max_length=30, blank=True, null=True)
    is_administrated_by_role = models.IntegerField(
        db_column="isAdministratedByRole"
    )
    psk = models.CharField(max_length=400, blank=True, null=True)
    ga = models.CharField(max_length=50, blank=True, null=True)
    ga_temporary_code = models.CharField(max_length=20)
    avatar = models.CharField(max_length=1000, blank=True, null=True)
    avatar_thumb = models.CharField(max_length=1000, blank=True, null=True)
    upgrade_needed = models.IntegerField()
    tree_load_strategy = models.CharField(max_length=30)
    can_manage_all_users = models.BooleanField(default=False)
    user_time_zone = models.CharField(max_length=50)
    agses_user_card_id = models.CharField(
        db_column="agses-usercardid", max_length=50
    )
    encrypted_psk = models.TextField(blank=True, null=True)
    user_ip = models.GenericIPAddressField()  # Changed to GenericIPAddressField for better validation
    user_ip_last_date = models.CharField(max_length=50, blank=True, null=True)
    yubico_user_key = models.CharField(max_length=100)
    yubico_user_id = models.CharField(max_length=100)
    public_key = models.TextField(blank=True, null=True)
    private_key = models.TextField(blank=True, null=True)
    special = models.CharField(max_length=250)
    auth_type = models.CharField(max_length=200)
    is_ready_for_usage = models.BooleanField(default=False)
    otp_provided = models.BooleanField(default=False)
    roles_from_ad_groups = models.CharField(max_length=1000, blank=True, null=True)
    ongoing_process_id = models.CharField(max_length=100, blank=True, null=True)
    mfa_enabled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    keys_recovery_time = models.CharField(max_length=500, blank=True, null=True)
    aes_iv = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = "users"

# Define a String method to make model strings human-readable
def __str__(self):
    return f"User {self.login}"

