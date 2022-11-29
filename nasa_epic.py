import os
import requests
import datetime
import expansion_extractor


def nasa_epic(api, path):
    if not os.path.exists(path):
        os.makedirs(path)
    parameters_1 = {
        'api_key': api,
    }
    response_1 = requests.get('https://api.nasa.gov/EPIC/api/natural/images',
                              params=parameters_1)
    response_1.raise_for_status()
    decoded_response = response_1.json()
    for order, dictionary in enumerate(decoded_response):
        date = (datetime.datetime.fromisoformat(dictionary['date']))
        image_name = dictionary['image']
        parameters_2 = {
            'api_key': api,
        }
        response_2 = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.month}/{date.day}/png/{image_name}.png',
            params=parameters_2)
        response_2.raise_for_status()
        exp = expansion_extractor.expansion_extractor(response_2.url)
        with open(os.path.join(path, f'nasa_epic_{order + 1}{exp}'), 'wb') as file:
            file.write(response_2.content)
