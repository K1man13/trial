# Generated by Django 5.1.2 on 2024-10-09 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_lnane_members_lname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='members',
            new_name='member',
        ),
    ]
