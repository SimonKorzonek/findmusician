# Generated by Django 3.1.3 on 2020-12-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20201202_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='kind',
        ),
        migrations.AddField(
            model_name='profile',
            name='kind',
            field=models.ManyToManyField(to='users.KindOfProfile'),
        ),
    ]