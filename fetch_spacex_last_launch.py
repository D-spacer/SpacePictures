import os
import requests
import expansion_extractor


def fetch_spacex_last_launch(id, path):
    os.makedirs(path, exist_ok=True)
    response_1 = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response_1.raise_for_status()
    decoded_response = response_1.json()
    for order, link in enumerate(decoded_response['links']['flickr']['original'], start=1):
        response_2 = requests.get(link)
        response_2.raise_for_status()
        exp = expansion_extractor.expansion_extractor(link)
        with open(os.path.join(path, f'spacex_{order + 1}{exp}'), 'wb') as file:
            file.write(response_2.content)
