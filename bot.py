import telegram
import random
import time


def publish_to_bot(telegram_chat_id, bot_token, timeout=14400):
    bot = telegram.Bot(token=bot_token)

    *_, content = os.walk('images')
    *_, pictures_to_publish = content
    random.shuffle(pictures_to_publish)
    while True:
        for picture in pictures_to_publish:
            with open(f'images/{photo}', 'rb') as image:
                bot.send_photo(chat_id=f'{telegram_chat_id}', photo=image)
            time.sleep(timeout)
