from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from file_manager.models import ImageFile

from .models import Place


class ImageInline(admin.TabularInline):
    model = ImageFile
    extra = 1


class PlacesAdmin(OSMGeoAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ["title"]
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlacesAdmin)
