from django.core.validators import ValidationError
from maps.utils import address_to_coords


def validate_exists_address(value):
    if not address_to_coords(value):
        raise ValidationError('Адрес не найден! Такое место точно существует?')
