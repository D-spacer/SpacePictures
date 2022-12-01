import telegram
import os
import random
import time


def publish_to_bot(timeout=14400):
    bot_token = os.environ['TG_BOT_TOKEN']
    telegram_chat_id = os.environ['TG_CHANNEL_ID']
    bot = telegram.Bot(token=bot_token)

    to_publish = []
    for obj in os.walk('images'):
        to_publish = obj[2]
    random.shuffle(to_publish)
    while True:
        for photo in to_publish:
            bot.send_photo(chat_id=f'{telegram_chat_id}', photo=open(f'images/{photo}', 'rb'))
            time.sleep(timeout)
