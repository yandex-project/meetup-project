from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from meetup_project.settings import BASE_DIR
from djeym.models import IconCollection, ClusterIcon, MarkerIcon, Placemark, CategoryPlacemark, Map, TileSource
import json
from slugify import slugify
import re
import base64


class Command(BaseCommand):
    help = 'Default map setup'

    def handle(self, *args, **options):
        cluster_icon = BASE_DIR / 'maps/static/maps/default_map_assets/default_cluster_icon.svg'
        with open(cluster_icon, "rb") as icon:
            icon_cluster = ClusterIcon.objects.create(svg=ContentFile(icon.read(), 'default_cluster_icon.svg'),
                                                      title='default',
                                                      )

        icon_collection = IconCollection.objects.create(title='default')

        marker_icon = BASE_DIR / 'maps/static/maps/default_map_assets/default_marker_icon.svg'
        with open(marker_icon, "rb") as icon:
            MarkerIcon.objects.create(svg=ContentFile(icon.read(), 'default_marker_icon.svg'),
                                      title='default',
                                      icon_collection=icon_collection)

        tile_sources = BASE_DIR / 'maps/static/maps/default_map_assets/Tile_Sources.json'
        with open(tile_sources) as json_file:
            source_list = json_file.read()
        source_list = json.loads(source_list)
        for source in source_list:
            if TileSource.objects.filter(slug=slugify(source['title'])).count() == 0:
                image_type = 'png' if re.search(
                    r'png', source['screenshot']) is not None else 'jpg'
                screenshot = re.sub(
                    r'^data:image/(png|jpeg);base64,', "", source['screenshot'])
                TileSource.objects.create(
                    title=source['title'],
                    maxzoom=source['maxzoom'],
                    minzoom=source['minzoom'],
                    source=source['source'],
                    screenshot=ContentFile(
                        base64.b64decode(screenshot), 'pic.' + image_type),
                    copyrights=source['copyrights'],
                    site=source['site'],
                    apikey=source['apikey'],
                    note=source['note']
                )

        ymap = Map.objects.create(title='default',
                                  icon_cluster=icon_cluster,
                                  icon_collection=icon_collection,
                                  tile=TileSource.objects.get(title='Google'),
                                  zoom=5,
                                  latitude='55.751619',  # координаты кремля как центр карты
                                  longitude='37.617891',
                                  )

        mark_category = CategoryPlacemark.objects.create(ymap=ymap,
                                                         title='default',
                                                         )

        Placemark.objects.create(ymap=ymap,
                                 category=mark_category,
                                 header='base',
                                 icon_slug='default',
                                 active=False
                                 )
