from django.db import models


class ImageFile(models.Model):
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)
