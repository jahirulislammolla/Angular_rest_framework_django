# Generated by Django 3.1.3 on 2020-11-30 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_laptop_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='image_name',
        ),
    ]