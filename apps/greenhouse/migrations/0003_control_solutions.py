# Generated by Django 2.1.5 on 2019-03-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
        ('greenhouse', '0002_auto_20190225_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='control',
            name='solutions',
            field=models.ManyToManyField(to='lab.Solution'),
        ),
    ]
