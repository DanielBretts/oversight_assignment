import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_images_by_location(api_key, bbox):
    url = f"https://graph.mapillary.com/images?access_token={api_key}&fields=id&bbox={bbox}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


if __name__ == "__main__":
    bbox = "12.967,55.597,13.008,55.607"
    images = get_images_by_location(os.getenv('MAPILLARY_API_KEY'), bbox)
    if images:
        print("Total images found:", len(images["data"]))
        for image in images["data"]:
            print("Image ID:", image["id"])
    else:
        print("Failed to retrieve images.")
