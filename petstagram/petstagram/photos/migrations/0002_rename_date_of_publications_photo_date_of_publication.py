# Generated by Django 4.2.1 on 2023-06-07 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='date_of_publications',
            new_name='date_of_publication',
        ),
    ]