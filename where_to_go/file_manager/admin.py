from django.contrib import admin

from .models import ImageFile


class PlacesAdmin(admin.ModelAdmin):
    list_display = ("image",)
    list_filter = ("image",)
    search_fields = ["image"]


admin.site.register(ImageFile, PlacesAdmin)
