import os
import requests


def download_file(url: str, filename: str) -> str:
    path = os.path.abspath(
        os.path.join(__file__, "../../files"))

    with open(os.path.join(path, filename), "wb") as file:
        with requests.get(url, stream=True) as r:

            for chunk in r.iter_content(chunk_size=8192):
                file.write(chunk)

    return os.path.join(path, filename)
