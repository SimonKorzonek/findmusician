# Generated by Django 3.1.3 on 2020-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201201_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='instruments',
        ),
        migrations.AddField(
            model_name='profile',
            name='instruments',
            field=models.ManyToManyField(to='users.Instrument'),
        ),
    ]
