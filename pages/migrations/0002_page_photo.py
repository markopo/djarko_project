# Generated by Django 3.1.1 on 2020-09-26 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='photo',
            field=models.ImageField(blank=True, upload_to='pages', verbose_name='Photo'),
        ),
    ]
