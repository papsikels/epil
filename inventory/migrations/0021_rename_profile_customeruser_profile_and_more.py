# Generated by Django 4.2.6 on 2023-12-01 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_rename_profile_customeruser_profile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customeruser',
            old_name='profile',
            new_name='Profile',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='customeruser',
            name='username',
        ),
    ]