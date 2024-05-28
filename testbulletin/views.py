from django.shortcuts import render
from django.views.generic.base import TemplateView

def MarkersMapView(request):
    return render(request, "testbulletin/templates/testbulletin/map.html")

# class MarkersMapView(TemplateView):
#     """Markers map view."""

#     template_name = "testbulletin/templates/testbulletin/map.html"