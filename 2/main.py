from telebot import telebot

bot = telebot.TeleBot("")

@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, "Добрый вечер, вы вошли в бот")

@bot.message_handler(commands=["now"])
def start(message, res=False):
    bot.send_message(message.chat.id, "ЭТО ДРУГОЕ СООБЩЕНИЕ")

bot.polling(none_stop=True, interval=0)
