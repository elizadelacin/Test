# Generated by Django 5.1.7 on 2025-04-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0036_quick_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather', models.CharField(max_length=255)),
                ('date_time', models.DateField()),
            ],
        ),
    ]
