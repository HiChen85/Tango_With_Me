# Generated by Django 2.1.5 on 2021-08-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='iframe_url',
            field=models.TextField(verbose_name='VideoURL'),
        ),
    ]
