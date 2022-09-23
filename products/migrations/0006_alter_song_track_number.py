# Generated by Django 3.2 on 2022-09-23 19:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_song_track_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
