# Generated by Django 3.2 on 2022-10-06 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_album_digital_download_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_group',
        ),
    ]
