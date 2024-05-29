import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from testbulletin.models import ModelGis
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from testbulletin.serializers import ModelGisSerializer
from django.core.serializers import serialize


def MarkersMapView(request):
    queryset = ModelGis.objects.all()
    context = {'queryset':queryset}
    context['queryset'] = json.loads(serialize('geojson', queryset))
    # print(context)
    return render(request, "testbulletin/templates/testbulletin/map.html", context)


class ModelGisListView(TemplateView):
    model = ModelGis
    template_name = 'testbulletin/templates/testbulletin/map.html'

    def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        modelgis = ModelGis.objects.all()
        context['modelgis'] = json.loads(serialize('geojson', modelgis))
        return context
    
# @api_view(['GET', 'POST'])
# # @authentication_classes([TokenAuthentication])
# @permission_classes((permissions.AllowAny,))
# def modelgis_list(request):
#     """
#     List all ModelGis ex
#     """
#     if request.method == 'GET':
       
#         modelgis = ModelGis.objects.all()
#         context['modelgis'] = json.loads(serialize('geojson', modelgis))
#         # serializer = ModelGisSerializer(modelgis, many=True)
#         print('request.__dict__', request.__dict__)
#         return context
#         # return Response( {
#         #        'data':serializer.data,
#         #      })
#     elif request.method == 'POST':
#         serializer = ModelGisSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
