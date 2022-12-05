import requests
import sys
import fetch_spacex_last_launch
import nasa_epic
import nasa_apod
import bot
import argparse
from dotenv import load_dotenv
import os


DIRECTORY = 'images'


def main():
    load_dotenv()
    epic_api_key = os.environ['EPIC_KEY']
    apod_api_key = os.environ['APOD_KEY']
    spacex_launch_id = os.environ['SPACEX_LAUNCH_ID']
    parser = argparse.ArgumentParser(description='keys for TG')
    parser.add_argument('chat_link', type=str, help='Input chat link')
    parser.add_argument('bot_id', type=str, help='Input bot id')
    args = parser.parse_args()
    try:
        tg_bot_id = args.bot_id
        tg_chat_link = args.url
        fetch_nasa_epic_images.fetch_nasa_epic_images(epic_api_key, DIRECTORY)
        fetch_spacex_last_launch.fetch_spacex_last_launch(spacex_launch_id, DIRECTORY)
        fetch_nasa_apod_images.fetch_nasa_apod_images(apod_api_key, DIRECTORY)
        bot.publish_to_bot(tg_chat_link, tg_bot_id)
    except requests.exceptions.HTTPError:
        sys.exit('Некорректный запрос')


if __name__ == "__main__":
    main()
