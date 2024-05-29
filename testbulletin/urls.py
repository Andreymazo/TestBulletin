from django.urls import path

from testbulletin.apps import TestbulletinConfig

from testbulletin.views import MarkersMapView#, ModelGisListView#    , modelgis_list

app_name = TestbulletinConfig.name

urlpatterns = [
    path("", MarkersMapView),
    # path("", ModelGisListView.as_view()),

]
