# Generated by Django 5.1.4 on 2025-01-03 12:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('encrypted_password', models.TextField()),
                ('password_iv', models.TextField()),
                ('encryption_type', models.CharField(default='AES', max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Password',
                'verbose_name_plural': 'Passwords',
                'db_table': 'passwords',
            },
        ),
        migrations.DeleteModel(
            name='CacheEntry',
        ),
        migrations.AlterModelOptions(
            name='folder',
            options={'verbose_name': 'Folder', 'verbose_name_plural': 'Folders'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='bloquer_creation',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='bloquer_modification',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='fa_icon',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='fa_icon_selected',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='nb_items_in_folder',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='nb_items_in_subfolders',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='nb_subfolders',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='nleft',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='nlevel',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='nright',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='personal_folder',
        ),
        migrations.RemoveField(
            model_name='folder',
            name='renewal_period',
        ),
        migrations.RemoveField(
            model_name='item',
            name='anyone_can_modify',
        ),
        migrations.RemoveField(
            model_name='item',
            name='auto_update_pwd_frequency',
        ),
        migrations.RemoveField(
            model_name='item',
            name='auto_update_pwd_next_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='complexity_level',
        ),
        migrations.RemoveField(
            model_name='item',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='item',
            name='email',
        ),
        migrations.RemoveField(
            model_name='item',
            name='fa_icon',
        ),
        migrations.RemoveField(
            model_name='item',
            name='id_tree',
        ),
        migrations.RemoveField(
            model_name='item',
            name='inactif',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_key',
        ),
        migrations.RemoveField(
            model_name='item',
            name='login',
        ),
        migrations.RemoveField(
            model_name='item',
            name='notification',
        ),
        migrations.RemoveField(
            model_name='item',
            name='perso',
        ),
        migrations.RemoveField(
            model_name='item',
            name='pw',
        ),
        migrations.RemoveField(
            model_name='item',
            name='pw_iv',
        ),
        migrations.RemoveField(
            model_name='item',
            name='pw_len',
        ),
        migrations.RemoveField(
            model_name='item',
            name='restricted_to',
        ),
        migrations.RemoveField(
            model_name='item',
            name='viewed_no',
        ),
        migrations.AddField(
            model_name='folder',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='folder',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='item',
            name='encrypted_password',
            field=models.TextField(default='default_encrypted_password'),
        ),
        migrations.AddField(
            model_name='item',
            name='password_iv',
            field=models.TextField(default='default_password_iv'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='manager.folder'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.customuser'),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='encryption_type',
            field=models.CharField(default='AES', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.folder'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='manager.customuser'),
        ),
        migrations.AlterField(
            model_name='process',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='process',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='processlog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='processlog',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='processtask',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='processtask',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterModelTable(
            name='folder',
            table='folders',
        ),
        migrations.AddField(
            model_name='password',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.folder'),
        ),
        migrations.AddField(
            model_name='password',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to='manager.customuser'),
        ),
        migrations.DeleteModel(
            name='CacheTree',
        ),
    ]
