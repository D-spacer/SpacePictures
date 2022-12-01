import requests
import sys
import fetch_spacex_last_launch
import nasa_epic
import nasa_apod
import bot
from dotenv import load_dotenv
import os


directory = 'images'


def main():
    load_dotenv()
    api_epic = os.environ['API_EPIC']
    api_apod = os.environ['API_APOD']
    spacex_id = os.environ['SPACEX_ID']
    try:
        nasa_epic.nasa_epic(api_epic, directory)
        fetch_spacex_last_launch.fetch_spacex_last_launch(spacex_id, directory)
        nasa_apod.nasa_apod(api_apod, directory)
        bot.publish_to_bot()
    except requests.exceptions.HTTPError:
        sys.exit('Некорректный запрос')


if __name__ == "__main__":
    main()
