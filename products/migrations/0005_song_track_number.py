# Generated by Django 3.2 on 2022-09-23 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_song_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='track_number',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
