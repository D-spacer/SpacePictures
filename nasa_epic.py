import os
import requests
import datetime
import expansion_extractor


def nasa_epic(api_key, path):
    os.makedirs(path, exist_ok=True)
    parameters_for_json = {
        'api_key': api_key,
    }
    response_for_json = requests.get('https://api.nasa.gov/EPIC/api/natural/images',
                              params=parameters_for_json)
    response_for_json.raise_for_status()
    decoded_response = response_for_json.json()
    for order, dictionary in enumerate(decoded_response, start=1):
        date = (datetime.datetime.fromisoformat(dictionary['date']))
        image_name = dictionary['image']
        parameters_for_image = {
            'api_key': api_key,
        }
        response_for_image = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.month}/{date.day}/png/{image_name}.png',
            params=parameters_2)
        response_for_image.raise_for_status()
        exp = expansion_extractor.expansion_extractor(response_for_image.url)
        with open(os.path.join(path, f'nasa_epic_{order + 1}{exp}'), 'wb') as file:
            file.write(response_for_image.content)
