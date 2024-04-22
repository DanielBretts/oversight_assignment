import os

import requests
from dotenv import load_dotenv

load_dotenv()


async def get_images_by_location(bbox):
    bbox_as_string = ','.join(str(value) for value in bbox.values())
    url = f"https://graph.mapillary.com/images?access_token={os.getenv('MAPILLARY_API_KEY')}&fields=id,computed_geometry&bbox={bbox_as_string}&limit=100"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


if __name__ == "__main__":
    bbox = "12.967,55.597,12.969,55.599"
    images = get_images_by_location(os.getenv('MAPILLARY_API_KEY'), bbox)
    if images:
        print("Total images found:", len(images["data"]))
        for image in images["data"]:
            print(f"Image ID: {image['id']}, {image['computed_geometry']['coordinates']}")
    else:
        print("Failed to retrieve images.")
