from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page
from blog.apps import BlogConfig
from config import settings
from .views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', cache_page(60)(BlogPostDetailView.as_view()), name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
