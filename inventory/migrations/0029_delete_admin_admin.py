# Generated by Django 4.2.6 on 2023-12-04 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_rename_adminuser_admin_alter_customeruser_is_staff'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
            ],
            options={
                'verbose_name': 'admin',
                'verbose_name_plural': 'admins',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('inventory.customeruser',),
        ),
    ]
