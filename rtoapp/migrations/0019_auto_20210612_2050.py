# Generated by Django 3.2.4 on 2021-06-12 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtoapp', '0018_userdetails_pollution_expiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='license_expiry',
            new_name='registration_expiry',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='license_number',
            new_name='registration_number',
        ),
    ]
