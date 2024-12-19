from django.urls import path

from .views import create_robot_apiview


urlpatterns = [
    path("create_robot/", create_robot_apiview, name="create-robot"),
]
