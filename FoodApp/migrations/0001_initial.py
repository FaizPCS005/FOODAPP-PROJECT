# Generated by Django 5.0.6 on 2024-07-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=122)),
                ('item_desc', models.CharField(max_length=122)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]