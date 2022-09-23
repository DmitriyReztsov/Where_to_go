from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=200)
    description_long = models.TextField(max_length=1000, blank=True)
    coordinates = models.PointField(srid=4326, geography=True, blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.lng and self.lat:
            self.coordinates = Point(self.lng, self.lat)
        elif self.coordinates:
            self.lng, self.lat = self.coordinates.coords
        super().save(*args, **kwargs)
