import random
import string

from django.db import models

from users.models import User
from django.utils.text import slugify
from unidecode import unidecode


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Meetup(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        help_text='Максимальная длинна 150'
    )

    date = models.DateTimeField(
        verbose_name='Дата'
    )

    description = models.TextField(
        verbose_name='Описание',
        max_length=500,
        help_text='Максимальная длинна 500'
    )

    place = models.CharField(
        verbose_name='Место',
        max_length=250,
        help_text='Максимальная длинна 250'
    )

    owner = models.ForeignKey(
        verbose_name='Создатель',
        to=User,
        related_name='my_meetups',
        null=True,
        on_delete=models.SET_NULL
    )

    lecturers = models.ManyToManyField(
        verbose_name='Лекторы',
        to=User,
        related_name='lectures'
    )

    users = models.ManyToManyField(
        verbose_name='Участники',
        to=User,
        related_name='meetups'
    )

    website = models.URLField(
        verbose_name='Сайт',
        blank=True
    )

    tags = models.ManyToManyField(
        verbose_name='Теги',
        to='Tag',
        related_name='meetups',
        blank=True
    )

    slug = models.SlugField(
        verbose_name='Slug',
        unique=True,
    )
    is_visible = models.BooleanField(
        verbose_name='Показывать?'
    )

    class Meta:
        verbose_name = 'Встерча'
        verbose_name_plural = 'Встречи'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name)) + '-' + rand_slug()
        super(Meetup, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=50,
        help_text='Максимальная длина 50'
    )

    parent = models.ForeignKey(
        verbose_name='Родитель',
        to='self',
        related_name='children',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
