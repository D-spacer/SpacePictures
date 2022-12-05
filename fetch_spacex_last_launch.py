import os
import requests
import extract_expansion


def fetch_spacex_last_launch(id, path):
    os.makedirs(path, exist_ok=True)
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    decoded_response = response.json()
    for order, link in enumerate(decoded_response['links']['flickr']['original'], start=1):
        response_for_image = requests.get(link)
        response_for_image.raise_for_status()
        exp = extract_expansion.extract_expansion(link)
        with open(os.path.join(path, f'spacex_{order + 1}{exp}'), 'wb') as file:
            file.write(response_for_image.content)
