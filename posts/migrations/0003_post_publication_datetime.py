# Generated by Django 3.1.3 on 2020-12-02 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication_datetime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
