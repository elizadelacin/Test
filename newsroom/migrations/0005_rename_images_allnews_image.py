# Generated by Django 5.1.7 on 2025-03-26 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0004_alter_mainnews_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allnews',
            old_name='images',
            new_name='image',
        ),
    ]
