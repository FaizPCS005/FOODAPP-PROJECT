# Generated by Django 5.0.6 on 2024-07-19 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0002_rename_item_desc_items1_item_desc1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='items1',
            name='item_image',
            field=models.CharField(default='', max_length=5000),
        ),
    ]