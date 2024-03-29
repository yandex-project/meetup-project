# Generated by Django 3.2.13 on 2022-04-30 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Максимальная длинна 150', max_length=150, verbose_name='Имя')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('description', models.TextField(help_text='Максимальная длинна 500', max_length=500, verbose_name='Описание')),
                ('place', models.CharField(help_text='Максимальная длинна 250', max_length=250, verbose_name='Место')),
                ('website', models.URLField(verbose_name='Сайт')),
                ('lecturers', models.ManyToManyField(related_name='lectures', to=settings.AUTH_USER_MODEL, verbose_name='Лекторы')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_meetups', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('users', models.ManyToManyField(related_name='meetups', to=settings.AUTH_USER_MODEL, verbose_name='Участники')),
            ],
            options={
                'verbose_name': 'Встерча',
                'verbose_name_plural': 'Встречи',
            },
        ),
    ]
