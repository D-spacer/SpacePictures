import os
import requests
import extract_expansion


def fetch_nasa_apod_images(api_key, path, pictures_number=30):
    os.makedirs(path, exist_ok=True)
    parameters = {
        'api_key': api_key,
        'count': pictures_number
    }
    response = requests.get('https://api.nasa.gov/planetary/apod',
                              params=parameters)
    response.raise_for_status()
    decoded_response = response.json()
    for order, dictionary in enumerate(decoded_response, start=1):
        response_for_image = requests.get(dictionary['url'])
        response_for_image.raise_for_status()
        exp = extract_expansion.extract_expansion(dictionary['url'])
        with open(os.path.join(path, f'nasa_apod_{order}{exp}'), 'wb') as file:
            file.write(response_for_image.content)
