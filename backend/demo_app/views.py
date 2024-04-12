from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from demo_app import custom_versions

# Normal view
def health_check(request, *args, **kwargs):
    return HttpResponse("Healthy | Demo App")


# API VIEWS
@api_view(["GET"])
def health_check_drf(request, *args, **kwargs):
    return Response(data={"msg": "Healthy | DRF"})


@api_view(["GET"])
def demo_version(request, *args, **kwargs):
    version = request.version
    return Response(data={"msg": f"You have hit {version} of demo-api"})

class DemoView(APIView):
    versioning_class = custom_versions.DemoViewVersion

    def get(self, request, *args, **kwargs):
        version = request.version
        return Response(data={"msg": f"You have hit {version}"})

class AnotherView(APIView):
    versioning_class = custom_versions.AnotherViewVersion

    def get(self, request, *args, **kwargs):
        version = request.version
        if version == "v1":
            # perform v1 related tasks
            return Response(data={"msg": "v1 logic"})
        elif version == "v2":
            # perform v2 related tasks
            return Response(data={"msg": "v2 logic"})
