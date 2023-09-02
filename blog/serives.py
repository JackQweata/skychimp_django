from django.core.cache import cache
from config import settings
from .models import BlogPost


def get_blog_post_cache():
    queryset = BlogPost.objects.order_by('-views')[:4]
    if settings.CACHE_ENABLED:
        key = 'blog_post'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = queryset
            cache.set(key, cache_data)

        return cache_data

    return queryset