# Generated by Django 4.1 on 2023-03-23 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data_fotogradia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='data_fotogradia',
            new_name='data_fotografia',
        ),
    ]
