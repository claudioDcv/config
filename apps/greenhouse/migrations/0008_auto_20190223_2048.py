# Generated by Django 2.1.5 on 2019-02-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0007_auto_20190223_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]