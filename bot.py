import telegram
from dotenv import load_dotenv
import os
import random
import time


def publish_to_bot(channel, timeout=14400):
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    
    bot = telegram.Bot(token=BOT_TOKEN)

    to_publish = []
    for obj in os.walk('images'):
        to_publish = obj[2]
    random.shuffle(to_publish)
    while True:
        for photo in to_publish:
            bot.send_photo(chat_id=f'{channel}', photo=open(f'images/{photo}', 'rb'))
            time.sleep(timeout)
