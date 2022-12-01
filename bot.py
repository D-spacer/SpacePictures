import telegram
import os
import random
import time


def publish_to_bot(timeout=14400):
    bot_token = os.environ['TG_BOT_TOKEN']
    telegram_chat_id = os.environ['TG_CHANNEL_ID']
    bot = telegram.Bot(token=bot_token)

    pictures_to_publish = []
    generator = os.walk('images')
    for object in generator:
        pictures_to_publish = object[2]
    random.shuffle(pictures_to_publish)
    while True:
        for picture in pictures_to_publish:
            bot.send_photo(chat_id=f'{telegram_chat_id}', photo=open(f'images/{picture}', 'rb'))
            time.sleep(timeout)
