from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ImageFile


class PlacesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
    )
    list_filter = (
        "id",
        "image",
    )
    search_fields = ["image"]
    readonly_fields = ["image_pic"]

    def image_pic(self, obj):
        return mark_safe(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.image.url,
                width=obj.image.width,
                height=obj.image.height,
            )
        )


admin.site.register(ImageFile, PlacesAdmin)
