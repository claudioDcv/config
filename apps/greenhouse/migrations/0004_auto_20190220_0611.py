# Generated by Django 2.1.5 on 2019-02-20 06:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('greenhouse', '0003_auto_20190220_0604'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='planttype',
            unique_together={('label', 'owner', 'sub_type')},
        ),
    ]
