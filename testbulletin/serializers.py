from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
)

from testbulletin.models import ModelGis


class ModelGisSerializer(
    GeoFeatureModelSerializer
):
    class Meta:
        fields = ("id", "name")
        geo_field = "location"
        model = ModelGis