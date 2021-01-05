# Generated by Django 3.1.3 on 2020-12-11 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20201211_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_published',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publication_datetime',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
    ]
