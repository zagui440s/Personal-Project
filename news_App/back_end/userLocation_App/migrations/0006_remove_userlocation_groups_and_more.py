# Generated by Django 5.1.4 on 2024-12-17 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userLocation_App', '0005_alter_userlocation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlocation',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userlocation',
            name='user_permissions',
        ),
    ]
