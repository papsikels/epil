# Generated by Django 4.2.6 on 2023-11-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_remove_customeruser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]