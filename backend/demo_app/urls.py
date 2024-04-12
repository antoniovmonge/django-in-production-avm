from django.urls import path
from demo_app import views

urlpatterns = [
    path("health-check", views.health_check),
    path("health-check-drf", views.health_check_drf),
    path("demo-version/", views.demo_version)
]
