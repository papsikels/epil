# Generated by Django 4.2.6 on 2023-11-30 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_customeruser_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
