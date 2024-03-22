# Generated by Django 4.2.10 on 2024-03-18 22:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_alter_story_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='Story_Cover',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]