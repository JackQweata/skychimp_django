from django import template
import os
from config import settings

register = template.Library()


@register.simple_tag
def mediapath(image_path):
    media_url = settings.MEDIA_URL
    return os.path.join(media_url, str(image_path))
