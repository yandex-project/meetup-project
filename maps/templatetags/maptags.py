# -*- coding: utf-8 -*-

from django import template

from djeym.models import Map
from djeym.views import vue_vendors_css_js
from urllib.parse import quote

register = template.Library()


@register.inclusion_tag('maps/includes/ymaps_front_filter.html')
def djeym_yandex_map_filter(slug, filters, lang='en'):
    """Load the map to the front page."""

    ymap = Map.objects.filter(slug=slug, active=True).first()
    filters = quote(str(filters).replace('\'', '\"'))
    ctx = {'ymap': ymap, 'filters': filters}
    if ymap is not None:
        general_settings = ymap.general_settings
        ctx['lang'] = lang or 'en',
        ctx['load_indicator'] = ymap.load_indicator
        ctx['load_indicator_size'] = ymap.load_indicator_size
        ctx['is_heatmap'] = ymap.heatmap_settings.active
        ctx['is_round_theme'] = general_settings.roundtheme
        ctx['width_map_front'] = general_settings.width_map_front
        ctx['height_map_front'] = general_settings.height_map_front
        ctx['presets'] = ymap.presets.values_list('js', flat=True)
        vue_vendors = vue_vendors_css_js('front')
        ctx.update(vue_vendors)
    return ctx


@register.simple_tag()
def static_map_url(meetup):
    # собираем ссылку для yandex maps static api
    base = 'https://static-maps.yandex.ru/1.x/?'
    type = 'map'  # тип карты: схема с названиями
    coords = meetup.marker.placemark.coordinates.strip('[]').split(',')
    coords.reverse()  # в placemark почему-то в другом порядке координаты
    coords = ','.join(coords)
    ll = coords  # координаты центра карты
    size = '400,300'  # размер изображения
    z = 15  # уровень масштабирования
    pt = coords + ',org'  # описание выводимой метки
    return f'{base}l={type}&ll={ll}&size={size}&z={z}&pt={pt}'
