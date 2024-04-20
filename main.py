import os

import folium
from folium import TileLayer
from dotenv import load_dotenv
from folium.plugins import VectorGridProtobuf
import mapbox_vector_tile

load_dotenv()
import requests


def create_map():
    m = folium.Map(location=[0, 0], zoom_start=2, width="80%", height="70%")

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

    pbf = folium.plugins.VectorGridProtobuf(url, "mapillary", options,overlay=True)
    # pbf.__dict__["overlay"] = True  # otherwise, TypeError
    pbf.add_to(m)

    folium.LayerControl().add_to(m)

    m.save("map.html") # uncomment to make an html
    print("Map with vector tiles saved as map_with_vector_tiles.html")

def fetch_mapillary_vector_tiles():
    import requests

    # Define the URL with placeholders for zoom (z), tile coordinates (x, y), and access token
    url = ("https://tiles.mapillary.com/maps/vtp/mly1_computed_public/2/{z}/{x}/{"
           "y}?access_token="+os.getenv('MAPILLARY_API_KEY'))

    # Replace the placeholders in the URL with the actual values

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data (e.g., save the tile image)
        tile_image = response.content
        # Further processing of the tile image...
    else:
        # Handle unsuccessful request (e.g., print error message)
        print("Error:", response.status_code)


if __name__ == "__main__":
    create_map()
