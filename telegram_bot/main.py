from telebot import telebot, types



bot = telebot.TeleBot("6075906387:AAG6rdo1UZlkl1QLjIg8aUamiW4CaRM0Nb4")


@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    print("Hello, World")

    item1 = types.KeyboardButton("/yes")
    item2 = types.KeyboardButton("/no")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, "Добрый вечер, вы вошли в бот", reply_markup=markup)


@bot.message_handler(commands=["yes"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    print("Hello, World")

    item1 = types.KeyboardButton("/yes")
    item2 = types.KeyboardButton("/no")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, "Вы нажали YES", reply_markup=markup)

@bot.message_handler(commands=["no"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, )
    print("Hello, World")

    item1 = types.KeyboardButton("/yes")
    item2 = types.KeyboardButton("/no")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, "Вы нажали NO", reply_markup=markup)

bot.polling(none_stop=True, interval=0)