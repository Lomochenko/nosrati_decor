# urls.py
from django.urls import path

from .views import robots_txt_view

urlpatterns = [
    path("robots.txt", robots_txt_view, name="robots_txt"),
]
