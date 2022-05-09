from django.contrib import admin
from maps.models import Marker


class MeetupMarkerInline(admin.StackedInline):
    model = Marker
    can_delete = False
    verbose_name = 'Маркер'
    verbose_name_plural = 'Маркеры'
