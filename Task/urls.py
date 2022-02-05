from django.urls import path

from . import views

# appname = "tasks"
urlpatterns = [

    path("", views.index, name="index"),
    path("add", views.add, name="add")
]