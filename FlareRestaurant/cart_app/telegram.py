import telepot

def send_message_tg(bot_token, chatid, message):
    bot = telepot.Bot(bot_token)
    bot.sendMessage(chatid, message)