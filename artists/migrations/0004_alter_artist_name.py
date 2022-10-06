# Generated by Django 3.2 on 2022-10-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(help_text='This name should be all lowercase, and contain no spaces, e.g. "forrest_records".', max_length=254),
        ),
    ]
