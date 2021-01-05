# Generated by Django 3.1.3 on 2020-12-11 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=60)),
                ('content', models.TextField(max_length=1200)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
