# Generated by Django 5.1.7 on 2025-03-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0010_allnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images/')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
