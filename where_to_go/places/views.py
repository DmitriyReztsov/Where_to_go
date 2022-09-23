from django.http import HttpResponse
from django.template import loader
import json

from places.models import Place


# TODO provide details
def get_details(id):
    place = Place.objects.get(id=id)
    data = {
        "title": place.title,
        "imgs": place.imagefile_set.all(),
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }



def index(request):
    template = loader.get_template("index.html")
    data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": obj.coordinates.coords
                },
                "properties": {
                    "title": obj.title,
                    "placeId": obj.id,
                    "detailsUrl": "./static/places/moscow_legends.json"
                }
            } for obj in Place.objects.all()
        ]
    }
    context = {"json_data": json.dumps(data)}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
