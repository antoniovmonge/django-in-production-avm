from django.urls import path
from demo_app import views

urlpatterns = [
    path("health-check", views.health_check),
    path("health-check-drf", views.health_check_drf),
    path("hello-world/", views.hello_world),
    path("demo-version/", views.demo_version),
    path("custom-version/", views.DemoView.as_view()),
    path("another-custom-version/", views.AnotherView.as_view()),
    path("apiview-class/", views.DemoAPIView.as_view()),
]
