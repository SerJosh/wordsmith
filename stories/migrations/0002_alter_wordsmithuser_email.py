# Generated by Django 4.2.10 on 2024-03-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordsmithuser',
            name='email',
            field=models.EmailField(max_length=40, verbose_name='User Email'),
        ),
    ]
