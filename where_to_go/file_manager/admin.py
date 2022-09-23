from django.contrib import admin

from .models import ImageFile


class PlacesAdmin(admin.ModelAdmin):
    list_display = ("id", "image",)
    list_filter = ("id", "image",)
    search_fields = ["image"]


admin.site.register(ImageFile, PlacesAdmin)
