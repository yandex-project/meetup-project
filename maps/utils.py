from djeym.models import Map
from meetup_project.settings import DJEYM_YMAPS_API_KEY
from yandex_geocoder import Client, NothingFound


# return the global map of meetups (the active one)
def get_global_map():
    return Map.objects.get(active=True)


def address_to_coords(address):
    geolocator = Client(DJEYM_YMAPS_API_KEY)
    try:
        coordinates = geolocator.coordinates(address)
        return f'[{float(coordinates[1])},{float(coordinates[0])}]'
    except NothingFound:
        return None
