# Generated by Django 2.2.12 on 2022-01-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0006_intake_track'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intake',
            old_name='fullname',
            new_name='name',
        ),
    ]
