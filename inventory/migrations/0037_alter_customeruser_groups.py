# Generated by Django 4.2.6 on 2023-12-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('inventory', '0036_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group', verbose_name='groups'),
        ),
    ]