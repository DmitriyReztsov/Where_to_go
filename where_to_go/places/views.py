import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse

from places.models import Place


def get_details(id):
    try:
        place = Place.objects.get(id=id)
    except ObjectDoesNotExist:
        return None
    data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.imagefile_set.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.lng, "lat": place.lat},
    }
    return data


def index(request):
    template = loader.get_template("index.html")
    data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": obj.coordinates.coords},
                "properties": {
                    "title": obj.title,
                    "placeId": obj.id,
                    "detailsUrl": reverse("places", args=[obj.id]),
                },
            }
            for obj in Place.objects.all()
        ],
    }
    context = {"json_data": json.dumps(data)}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def places(request, id):
    data = get_details(id)
    if data:
        return JsonResponse(
            data, json_dumps_params={"ensure_ascii": False, "indent": 4}
        )
    return HttpResponseNotFound("Not found")
