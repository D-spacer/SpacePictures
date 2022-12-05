import requests
import sys
import fetch_spacex_last_launch
import nasa_epic
import nasa_apod
import bot
from dotenv import load_dotenv
import os


DIRECTORY = 'images'


def main():
    load_dotenv()
    epic_api_key = os.environ['EPIC_KEY']
    apod_api_key = os.environ['APOD_KEY']
    spacex_launch_id = os.environ['SPACEX_LAUNCH_ID']
    try:
        fetch_nasa_epic_images.fetch_nasa_epic_images(epic_api_key, DIRECTORY)
        fetch_spacex_last_launch.fetch_spacex_last_launch(spacex_launch_id, DIRECTORY)
        fetch_nasa_apod_images.fetch_nasa_apod_images(apod_api_key, DIRECTORY)
        bot.publish_to_bot('@space_pictures_generator', '5866680710:AAF8Xfd3EEfyjn0vCFeCEYE-XrgAyYUC9Ns')
    except requests.exceptions.HTTPError:
        sys.exit('Некорректный запрос')


if __name__ == "__main__":
    main()
