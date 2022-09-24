from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("places/<int:id>/", views.places, name="places"),
]
