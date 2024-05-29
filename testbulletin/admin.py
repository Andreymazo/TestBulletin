
from django.contrib.gis import admin

from testbulletin.models import ModelGis


@admin.register(ModelGis)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "location")
