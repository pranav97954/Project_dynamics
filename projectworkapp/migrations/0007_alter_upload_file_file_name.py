# Generated by Django 4.0.4 on 2023-01-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectworkapp', '0006_delete_uploadfiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_file',
            name='file_name',
            field=models.CharField(max_length=255),
        ),
    ]
