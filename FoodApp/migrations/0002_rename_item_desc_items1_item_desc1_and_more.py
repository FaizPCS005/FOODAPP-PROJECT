# Generated by Django 5.0.6 on 2024-07-18 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items1',
            old_name='item_desc',
            new_name='item_desc1',
        ),
        migrations.RenameField(
            model_name='items1',
            old_name='item_name',
            new_name='item_name1',
        ),
        migrations.RenameField(
            model_name='items1',
            old_name='item_price',
            new_name='item_price1',
        ),
    ]
