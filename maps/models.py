from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from meetups.models import Meetup
from djeym.models import Placemark
from maps.utils import address_to_coords


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


# @receiver(post_save, sender=Meetup)
# def create_meetup_placemark(sender, instance, created, **kwargs):
#     if created:
#         base = Placemark.objects.get(header='base')
#         mark = Placemark.objects.create(
#                                         ymap=base.ymap,
#                                         category=base.category,
#                                         header=instance.name,
#                                         body=instance.description,
#                                         footer=instance.date,
#                                         coordinates=address_to_coords(instance.place),
#                                         icon_slug=base.icon_slug
#         )
#         Marker.objects.create(meetup=instance, placemark=mark)
#
#
# @receiver(post_save, sender=Meetup)
# def save_meetup_placemark(sender, instance, **kwargs):
#     instance.marker.save()
