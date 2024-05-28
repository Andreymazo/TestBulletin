from django.urls import path

from testbulletin.apps import TestbulletinConfig

from .views import MarkersMapView

app_name = TestbulletinConfig.name

urlpatterns = [
    path("", MarkersMapView.as_view()),
]
