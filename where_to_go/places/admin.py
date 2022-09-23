from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.utils.safestring import mark_safe

from file_manager.models import ImageFile

from .models import Place


class ImageInline(SortableStackedInline):
    model = ImageFile
    extra = 1
    fields = ["image", "image_preview", "position"]
    readonly_fields = [
        "image_preview",
    ]

    def image_preview(self, obj):
        return mark_safe(
            '<img src="{url}" style="max-height: 200px;" />'.format(url=obj.image.url)
        )


class PlacesAdmin(SortableAdminBase, OSMGeoAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ["title"]
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlacesAdmin)
