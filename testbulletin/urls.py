from django.urls import path

from testbulletin.apps import TestbulletinConfig

from testbulletin.views import MarkersMapView

app_name = TestbulletinConfig.name

urlpatterns = [
    path("", MarkersMapView),
    # path("", MarkersMapView.as_view()),
]
