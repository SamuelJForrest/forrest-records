# Generated by Django 3.2 on 2022-10-01 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_song_track_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='digital_download_price',
        ),
    ]