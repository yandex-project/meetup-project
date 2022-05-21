from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from meetups.models import Meetup
from djeym.models import Placemark, CategoryPlacemark
from maps.utils import get_global_map, address_to_coords


class Marker(models.Model):
    meetup = models.OneToOneField(
        Meetup,
        on_delete=models.CASCADE,
        related_name='marker'
    )
    placemark = models.OneToOneField(
        Placemark,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='marker'
    )

    def __str__(self):
        return f'Marker for meetup {self.meetup}'


@receiver(post_save, sender=Meetup)
def create_meetup_placemark(sender, instance, created, **kwargs):
    if created:
        mark = Placemark.objects.create(ymap=get_global_map(),
                                        category=CategoryPlacemark.objects.get(active=True),
                                        header=instance.name,
                                        body=instance.description,
                                        footer=instance.date,
                                        coordinates=address_to_coords(instance.place),
                                        icon_slug='education')
        Marker.objects.create(meetup=instance, placemark=mark)


@receiver(post_save, sender=Meetup)
def save_meetup_placemark(sender, instance, **kwargs):
    instance.marker.placemark.save()
    instance.marker.save()
