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
    API_EPIC = os.environ['API_EPIC']
    API_APOD = os.environ['API_APOD']
    SPACEX_ID = os.environ['SPACEX_ID']
    try:
        nasa_epic.nasa_epic(API_EPIC, directory)
        fetch_spacex_last_launch.fetch_spacex_last_launch(SPACEX_ID, directory)
        nasa_apod.nasa_apod(API_APOD, directory)
        bot.publish_to_bot()
    except requests.exceptions.HTTPError:
        sys.exit('Неверная ссылка')


if __name__ == "__main__":
    main()