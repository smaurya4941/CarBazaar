# Generated by Django 5.1.7 on 2025-03-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.CharField(default='UP', max_length=100),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
