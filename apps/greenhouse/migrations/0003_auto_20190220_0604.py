# Generated by Django 2.1.5 on 2019-02-20 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0002_planttype_sub_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planttype',
            name='created',
        ),
        migrations.RemoveField(
            model_name='planttype',
            name='updated',
        ),
    ]
