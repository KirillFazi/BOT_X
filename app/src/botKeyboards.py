from telebot import types
from BotConfig import bot


def create_start_keyboard(chatId, text):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    button1 = types.KeyboardButton(text="Столовая")
    button2 = types.KeyboardButton(text="Запрос")
    button3 = types.KeyboardButton(text="Отзыв")

    markup.add(button1, button2, button3)

    bot.send_message(chatId, text, reply_markup=markup)


def create_dining_room_keyboard(chatId, text):
    markup = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="Закончилась вода", callback_data="water")
    button2 = types.InlineKeyboardButton(text="Закончились приборы", callback_data="tableware")
    button3 = types.InlineKeyboardButton(text="Закончились тарелки", callback_data="plates")
    button4 = types.InlineKeyboardButton(text="Другой запрос", callback_data="dining_room_request")
    button5 = types.InlineKeyboardButton(text="В главное меню", callback_data="menu")

    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    bot.send_message(chatId, text, reply_markup=markup)


def create_request_keyboard(chatId, text):
    markup = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text="Пространство", callback_data="space")
    button2 = types.InlineKeyboardButton(text="Культ. масс.", callback_data="event")
    button3 = types.InlineKeyboardButton(text="Связь", callback_data="communication")
    button4 = types.InlineKeyboardButton(text="В главное меню", callback_data="menu")

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)

    bot.send_message(chatId, text, reply_markup=markup)



