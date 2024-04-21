import os

import folium
from folium import TileLayer
from dotenv import load_dotenv
from folium.plugins import VectorGridProtobuf
import mapbox_vector_tile

load_dotenv()
import requests


def create_map():
    map = folium.Map(location=[0, 0], zoom_start=2, width="80%", height="70%")

    url = (
        "https://tiles.mapillary.com/maps/vtp/"
        "mly1_public/2/{z}/{x}/{y}?access_token={token}"
    )

    options = {
        "token": os.getenv("MAPILLARY_API_KEY"),
        "vectorTileLayerStyles": {
            "overview": {
                "fill": True,
                "radius": 5,
                "color": "#e87147",
                "opacity": 0.6,
            },
        },
    }

    pbf = folium.plugins.VectorGridProtobuf(url, "mapillary", options, overlay=True)

    pbf.add_to(map)

    folium.LayerControl().add_to(map)

    map.save("map.html")
    print("Map with vector tiles saved as map_with_vector_tiles.html")


if __name__ == "__main__":
    create_map()

