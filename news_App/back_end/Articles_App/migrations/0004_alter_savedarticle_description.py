# Generated by Django 5.1.4 on 2024-12-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles_App', '0003_alter_savedarticle_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedarticle',
            name='description',
            field=models.TextField(blank=True, default='No description provided', null=True),
        ),
    ]
