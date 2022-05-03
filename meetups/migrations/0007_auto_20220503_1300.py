# Generated by Django 3.2.13 on 2022-05-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0006_alter_meetup_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Показывать?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetup',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]
