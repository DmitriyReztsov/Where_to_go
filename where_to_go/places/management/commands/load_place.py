import json
import os

import requests
from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from file_manager.models import ImageFile
from places.models import Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("path_to_jsons", nargs="+", type=str)

    def handle(self, *args, **options):
        path_to_jsons = options["path_to_jsons"][0]
        jsons_list = os.listdir(path_to_jsons)
        for json_file in jsons_list:
            with open(path_to_jsons + json_file, "r") as file:
                init_data = json.load(file)
                imgs = init_data.pop("imgs")
                coords = init_data.pop("coordinates")
                place, created = Place.objects.get_or_create(**init_data)
                place.coordinates = Point(float(coords["lng"]), float(coords["lat"]))
                place.save()
                if created:
                    self._process_imgs(imgs, place)

    def _process_imgs(self, imgs, place):
        for num, img in enumerate(imgs):
            image_file = requests.get(img)
            file_name = img.split("/")[-1]
            ImageFile.objects.get_or_create(
                image=ContentFile(image_file.content, file_name),
                place=place,
                position=num,
            )
