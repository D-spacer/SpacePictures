import telegram


bot = telegram.Bot(token='5866680710:AAF8Xfd3EEfyjn0vCFeCEYE-XrgAyYUC9Ns')
print(bot.get_me())
bot.send_message(chat_id='@space_pictures_generator', text="Welcome to Space Pictures.")