# Generated by Django 3.1.3 on 2020-12-26 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20201206_2105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instrument',
            new_name='UserCooperation',
        ),
        migrations.RenameModel(
            old_name='KindOfProfile',
            new_name='UserGenere',
        ),
        migrations.RenameModel(
            old_name='Cooperation',
            new_name='UserInstrument',
        ),
        migrations.RenameModel(
            old_name='Genere',
            new_name='UserKindOfProfile',
        ),
    ]