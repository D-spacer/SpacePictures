import os
import requests
import expansion_extractor


def nasa_apod(api_key, path, pictures_number=30):
    os.makedirs(path, exist_ok=True)
    parameters = {
        'api_key': api_key,
        'count': pictures_number
    }
    response_for_json = requests.get('https://api.nasa.gov/planetary/apod',
                              params=parameters)
    response_for_json.raise_for_status()
    decoded_response = response_for_json.json()
    for order, dictionary in enumerate(decoded_response, start=1):
        response_for_image = requests.get(dictionary['url'])
        response_for_image.raise_for_status()
        exp = expansion_extractor.expansion_extractor(dictionary['url'])
        with open(os.path.join(path, f'nasa_apod_{order + 1}{exp}'), 'wb') as file:
            file.write(response_for_image.content)
