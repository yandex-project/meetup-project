from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from meetups.models import Meetup
from djeym.models import Placemark


class Marker(models.Model):
    meetup = models.OneToOneField(Meetup, on_delete=models.CASCADE)
    placemark = models.OneToOneField(Placemark, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=Meetup)
def create_meetup_placemark(sender, instance, created, **kwargs):
    if created:
        Marker.objects.create(meetup=instance)


@receiver(post_save, sender=Meetup)
def save_meetup_placemark(sender, instance, **kwargs):
    instance.marker.save()