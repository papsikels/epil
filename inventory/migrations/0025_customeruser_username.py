# Generated by Django 4.2.6 on 2023-12-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0024_customeruser_groups_customeruser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeruser',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]