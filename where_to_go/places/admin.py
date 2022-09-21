from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Place


class PlacesAdmin(OSMGeoAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ["title"]


admin.site.register(Place, PlacesAdmin)
