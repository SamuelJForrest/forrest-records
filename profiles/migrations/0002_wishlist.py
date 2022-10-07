# Generated by Django 3.2 on 2022-10-07 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_product_group'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
            ],
            options={
                'verbose_name_plural': 'Wishlist',
            },
        ),
    ]
