# Generated by Django 3.1.7 on 2021-03-31 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image_height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='images',
            name='image_width',
            field=models.IntegerField(),
        ),
    ]
