# Generated by Django 4.2.6 on 2023-12-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0026_adminuser_is_active_adminuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
