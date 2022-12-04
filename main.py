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
    epic_api_key = os.environ['EPIC_KEY']
    apod_api_key = os.environ['APOD_KEY']
    spacex_launch_id = os.environ['SPACEX_LAUNCH_ID']
    try:
        nasa_epic.nasa_epic(epic_api_key, directory)
        fetch_spacex_last_launch.fetch_spacex_last_launch(spacex_launch_id, directory)
        nasa_apod.nasa_apod(apod_api_key, directory)
        bot.publish_to_bot(telegram_chat_id='@space_pictures_generator')
    except requests.exceptions.HTTPError:
        sys.exit('Некорректный запрос')


if __name__ == "__main__":
    main()
