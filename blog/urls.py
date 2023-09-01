from django.urls import path
from blog.apps import BlogConfig
from .views import *

app_name = BlogConfig.name

urlpatterns = [
    path('', index, name='home'),
    path('blogs/', ..., name='blogs')
]
