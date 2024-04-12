from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def health_check(request, *args, **kwargs):
    return HttpResponse("Healthy | Demo App")

@api_view(['GET'])
def health_check_drf(request, *args, **kwargs):
    return Response(data={"msg": "Healthy | DRF"})
