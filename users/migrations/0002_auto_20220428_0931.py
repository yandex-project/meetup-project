# Generated by Django 3.2.13 on 2022-04-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание профиля'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
