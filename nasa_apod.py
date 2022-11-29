import os
import requests
import expansion_extractor


def nasa_apod(api, path):
    if not os.path.exists(path):
        os.makedirs(path)
    parameters = {
        'api_key': api,
        'count': 30
    }
    response_1 = requests.get('https://api.nasa.gov/planetary/apod',
                              params=parameters)
    response_1.raise_for_status()
    decoded_response = response_1.json()
    for order, dictionary in enumerate(decoded_response):
        response_2 = requests.get(dictionary['url'])
        response_2.raise_for_status()
        exp = expansion_extractor.expansion_extractor(dictionary['url'])
        with open(os.path.join(path, f'nasa_apod_{order + 1}{exp}'), 'wb') as file:
            file.write(response_2.content)
