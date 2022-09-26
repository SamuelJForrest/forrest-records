# Generated by Django 3.2 on 2022-09-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_alter_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='friendly_name',
            field=models.CharField(help_text='This should be the artist name you want users to see.', max_length=254),
        ),
    ]
