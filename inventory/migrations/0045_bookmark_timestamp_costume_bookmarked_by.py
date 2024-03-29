# Generated by Django 5.0 on 2024-01-25 23:49

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0044_alter_costume_date_created_alter_message_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='costume',
            name='bookmarked_by',
            field=models.ManyToManyField(related_name='bookmarks', through='inventory.Bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]
