# Generated by Django 3.1 on 2021-02-05 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competence', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='niveaux',
            old_name='niveaux',
            new_name='competence',
        ),
    ]
