# Generated by Django 4.2.10 on 2024-03-23 18:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_alter_story_story_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='Story_Cover',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='Story Cover'),
        ),
    ]
