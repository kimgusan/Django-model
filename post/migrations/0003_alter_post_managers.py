# Generated by Django 5.0.2 on 2024-02-21 13:51

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_member_alter_post_post_content'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('enabled_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
