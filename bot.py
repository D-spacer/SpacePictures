import telegram
from dotenv import load_dotenv
import os
import random
import time


def publish_to_bot():
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    timeout = os.environ['TIMEOUT']
    channel=os.environ['CHANNEL']
    bot = telegram.Bot(token=BOT_TOKEN)

    to_publish = []
    for obj in os.walk('images'):
        to_publish = obj[2]
    random.shuffle(to_publish)
    while True:
        for photo in to_publish:
            bot.send_photo(chat_id=f'{CHANNEL}', photo=open(f'images/{photo}', 'rb'))
            time.sleep(int(TIMEOUT))
