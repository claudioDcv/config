# Generated by Django 2.1.5 on 2019-02-09 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('greenhouse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='purchase_history',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]