# Generated by Django 3.1.3 on 2020-12-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20201202_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='agsdg', max_length=300),
            preserve_default=False,
        ),
    ]
