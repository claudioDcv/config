# Generated by Django 2.1.5 on 2019-02-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenhouse', '0013_auto_20190211_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='humidity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
