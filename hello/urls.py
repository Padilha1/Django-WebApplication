from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("padilha", views.padilha, name="padilha"),
    path("<str:name>", views.greet, name="greet")
]