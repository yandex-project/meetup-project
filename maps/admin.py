from django.contrib import admin
from djeym.models import Statistics, BlockedIP, Polyline, Polygon, HeatPoint
from maps.models import Marker


admin.site.unregister((BlockedIP,
                       Statistics,
                       Polyline,
                       Polygon,
                       HeatPoint,
                       ))


class MeetupMarkerInline(admin.StackedInline):
    model = Marker
    can_delete = False
    verbose_name = 'Маркер'
    verbose_name_plural = 'Маркеры'
