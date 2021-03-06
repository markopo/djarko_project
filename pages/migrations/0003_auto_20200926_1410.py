# Generated by Django 3.1.1 on 2020-09-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='permalink',
        ),
        migrations.AddField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
