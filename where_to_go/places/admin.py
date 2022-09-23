from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Place
from file_manager.models import ImageFile


class ImageInline(admin.TabularInline):
    model = ImageFile


class PlacesAdmin(OSMGeoAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ["title"]
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlacesAdmin)
