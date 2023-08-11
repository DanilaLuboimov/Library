import os
import requests

from PIL import Image, UnidentifiedImageError


def download_image(url: str, path: str, img_id: int) -> str:
    res = requests.get(url, stream=True).raw

    path = os.path.abspath(
        os.path.join(
            __file__, f"{path}/{img_id}/{img_id}.jpeg"
        )
    )
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        img = Image.open(res)
        img.save(path, "jpeg")
    except UnidentifiedImageError:
        return None

    return os.path.abspath(path)
