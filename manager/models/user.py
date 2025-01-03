from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class CustomUser(User):
    # id = models.AutoField(primary_key=True)
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
    # email = models.CharField(max_length=300, default="none")
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
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
    deleted_at = models.CharField(max_length=30, null=True)
    keys_recovery_time = models.CharField(max_length=500, null=True)
    aes_iv = models.TextField(null=True)

    class Meta:
        db_table = "customuser"
