from django.core.exceptions import ValidationError


def defaultLevel(value):
    if value == 'no_levels':
        raise ValidationError("Please select level")
    return value
