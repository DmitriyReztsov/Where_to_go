from django.conf import settings
from django.db import models


class ImageFile(models.Model):
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(
        "places.Place", on_delete=models.SET_NULL, blank=True, null=True
    )
