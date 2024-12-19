from django.urls import path

from .views import export_robots_stat_view

urlpatterns = [
    path("export_robots_stat/", export_robots_stat_view, name="export-robots-stat"),
]
