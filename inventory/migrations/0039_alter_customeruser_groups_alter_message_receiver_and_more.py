# Generated by Django 4.2.6 on 2023-12-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('inventory', '0038_alter_customeruser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customeruser_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', related_query_name='received_message', to='inventory.customeruser'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', related_query_name='sent_message', to='inventory.customeruser'),
        ),
    ]