# Generated by Django 3.2.3 on 2021-06-02 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtoapp', '0003_auto_20210602_0522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='licence_expiry',
            new_name='license_expiry',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='licence_number',
            new_name='license_number',
        ),
    ]