# Generated by Django 3.2.4 on 2021-06-12 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtoapp', '0007_auto_20210612_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='reg_expiry',
            new_name='registration_expiry',
        ),
    ]
