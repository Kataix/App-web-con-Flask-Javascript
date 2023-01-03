import telegram
tok =  '5321661491:AAEp4aqnSTAHoYiWsHLDvTKTsDhAcxMy54k'
chatId = '5928211889'

bot = telegram.Bot(token = tok)
print(bot.get_me())
bot.sendMessage('chat_id=chatId, photo=f')

with open('graft1.jpg','rb') as f:
    bot.sendPhoto(chat_id=chatId, photo=f)
