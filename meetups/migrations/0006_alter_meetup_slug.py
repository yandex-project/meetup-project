# Generated by Django 3.2.13 on 2022-05-03 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_auto_20220503_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='slug',
            field=models.SlugField(allow_unicode=True, verbose_name='Slug'),
        ),
    ]
