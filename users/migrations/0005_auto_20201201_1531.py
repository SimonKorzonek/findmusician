# Generated by Django 3.1.3 on 2020-12-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201201_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instruments',
            field=models.ManyToManyField(related_name='profile', to='users.Instrument'),
        ),
    ]
