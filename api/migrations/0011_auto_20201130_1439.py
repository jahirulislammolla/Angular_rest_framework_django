# Generated by Django 3.1.3 on 2020-11-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_laptop_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='image_name',
        ),
        migrations.AddField(
            model_name='laptop',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
