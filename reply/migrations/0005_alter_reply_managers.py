# Generated by Django 5.0.2 on 2024-02-21 13:51

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reply', '0004_rename_secret_reply_reply_reply_private_status_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='reply',
            managers=[
                ('enabled_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]