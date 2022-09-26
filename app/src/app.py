from BotConfig import bot
from BotConfig import start_text
from BotConfig import help_text
from BotConfig import error_text
from BotConfig import KirillBiruylinId
from BotConfig import sphereId
from BotConfig import replay_text_water
from BotConfig import request_text
from BotConfig import request_text_space
from BotConfig import request_text_event
from BotConfig import request_text_communication
from BotConfig import answer_to_request
from BotConfig import answer_to_dining_room

from botKeyboards import create_start_keyboard
from botKeyboards import create_dining_room_keyboard
from botKeyboards import create_request_keyboard

callbackId = 0


@bot.message_handler(commands=["start", "go"])
def start_message(message):
    create_start_keyboard(message.chat.id, start_text)


@bot.message_handler(commands=["help"])
def help_message(message):
    create_start_keyboard(message.chat.id, help_text)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global callbackId
    data = call.data
    userId = call.from_user.id

    if data == "water":
        bot.send_message(KirillBiruylinId, "Вода закончилось. Нужно заказать.")
        create_start_keyboard(userId, answer_to_dining_room)

    elif data == "tableware":
        print(userId)
        bot.send_message(sphereId["space"], "Закончились столовые приборы. Нужно купить.")
        create_start_keyboard(userId, answer_to_dining_room)

    elif data == "plates":
        print(userId)
        bot.send_message(sphereId["space"], "Закончились тарлеки. Нужно купить.")
        create_start_keyboard(userId, answer_to_dining_room)

    elif data == "dining_room_request":
        create_start_keyboard(userId, request_text)
        callbackId = 1

    elif data == "space":
        create_start_keyboard(userId, request_text_space)
        callbackId = 2

    elif data == "event":
        create_start_keyboard(userId, request_text_event)
        callbackId = 3

    elif data == "communication":
        create_start_keyboard(userId, request_text_communication)
        callbackId = 4

    elif data == "menu":
        create_start_keyboard(userId, "Главное меню")

    bot.delete_message(userId, call.message.id)


@bot.message_handler(content_types='text')
def button_message(message):
    global callbackId
    chatText = message.text.lower()
    chatId = message.chat.id
    userName = message.from_user.username
    text = message.text

    if chatText == "столовая":
        print('Столовая')
        create_dining_room_keyboard(chatId, "Столовая")

    elif chatText == "запрос":
        print('Запрос')
        create_request_keyboard(chatId, "Запрос")

    elif chatText == "отзыв":
        print('Отзыв')
        create_start_keyboard(chatId, "Оставьте свой отзыв: ")
        callbackId = 5

    elif chatText == "заказал воду":
        bot.send_message(KirillBiruylinId, replay_text_water)

    elif callbackId == 1:
        bot.send_message(sphereId["space"], "Запрос в столовую: {0} \nuserName: {1}".format(text, userName))
        bot.send_message(chatId, answer_to_request)
        callbackId = 0

    elif callbackId == 2:
        bot.send_message(sphereId["space"], "Запрос в сферу пространства: {0} \nuserName: {1}".format(text, userName))
        bot.send_message(chatId, answer_to_request)
        callbackId = 0

    elif callbackId == 3:
        bot.send_message(sphereId["event"], "Запрос в сферу культ. масс.: {0} \nuserName: {1}".format(text, userName))
        bot.send_message(chatId, answer_to_request)
        callbackId = 0

    elif callbackId == 4:
        bot.send_message(sphereId["communication"], "Запрос в сферу связи: {0} \nuserName: {1}".format(text, userName))
        bot.send_message(chatId, answer_to_request)
        callbackId = 0

    elif callbackId == 5:
        bot.send_message(sphereId["studX"], "Отзыв: {0} \nuserName: {1}".format(text, userName))
        bot.send_message(chatId, "Спасибо за твой отзыва! Для нас это очень важно.")
        callbackId = 0

    else:
        bot.send_message(message.chat.id, error_text)

    bot.send_message(sphereId["test"], "{0} : {1}".format(userName, message.text))


if __name__ == "__main__":
    bot.infinity_polling()
