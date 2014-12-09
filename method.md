To search coordinates for address. Use the nominatim of openstreetmaps:

This address:  Av. La Paz 300 La Perla appended to the URL:

http://nominatim.openstreetmap.org/?format=json&addressdetails=1&q=Av.%20La%20paz%20300%20La%20Perla&format=json&limit=1

gives this:

```
[
    {
        "place_id": "2636945172",
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright",
        "osm_type": "way",
        "osm_id": "315236389",
        "boundingbox": [
            "-12.0762661",
            "-12.0732752",
            "-77.121424",
            "-77.1132489"
        ],
        "lat": "-12.0756958",
        "lon": "-77.1148077",
        "display_name": "Avenida La Paz, La Perla, Callao, Constitutional Province of Callao, 07006, Peru",
        "class": "highway",
        "type": "residential",
        "importance": 0.6,
        "address": {
            "road": "Avenida La Paz",
            "suburb": "La Perla",
            "city": "La Perla",
            "county": "Callao",
            "state": "Constitutional Province of Callao",
            "postcode": "07006",
            "country": "Peru",
            "country_code": "pe"
        }
    }
]
```

extact coordinates of each plot and make a heatmap in GoogleMAps
