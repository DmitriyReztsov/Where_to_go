from django.db import models


class ImageFile(models.Model):
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)
    place = models.ForeignKey(
        "places.Place",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    position = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["position", "created_on"]
