# Generated by Django 2.1.5 on 2019-02-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0002_plant_purchase_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='slug',
            field=models.SlugField(default=1, max_length=140, unique=True),
            preserve_default=False,
        ),
    ]