# Generated by Django 3.1.3 on 2020-11-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_laptop_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='image_name',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]