# Generated by Django 3.1.3 on 2020-12-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='kutas', max_length=1200),
            preserve_default=False,
        ),
    ]
