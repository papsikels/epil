# Generated by Django 4.2.6 on 2023-11-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_customeruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdultCostume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='costume_photos/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='costume_photos/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='costume_photos/')),
                ('status', models.CharField(choices=[('adult', 'Adult'), ('child', 'Child')], max_length=5)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChildCostume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='costume_photos/')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='costume_photos/')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='costume_photos/')),
                ('status', models.CharField(choices=[('adult', 'Adult'), ('child', 'Child')], max_length=5)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
