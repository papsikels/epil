# Generated by Django 4.2.6 on 2023-11-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_adminuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='password',
        ),
    ]
