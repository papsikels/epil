# Generated by Django 4.2.6 on 2023-12-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('inventory', '0041_remove_customeruser_status_customeruser_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='user',
        ),
        migrations.AddField(
            model_name='customeruser',
            name='status',
            field=models.CharField(choices=[('user', 'User'), ('staff', 'Staff'), ('superuser', 'Superuser')], default='user', max_length=10),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customeruser_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customeruser_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
