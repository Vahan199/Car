# Generated by Django 4.0.6 on 2022-07-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_car_is_published_car_time_create_car_time_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
