import telebot
from bot_token import token

callbackId = 0

bot = telebot.TeleBot(token)

KirillBiruylinId = "504747701"
pId = "1686106185"
# -794669285
sphereId = {
    "communication": "-699610490",
    "space": "-1001764457618",
    "event": "-692349819",
    "test": "-793685251",
    "studX": "-1001621769831"
}

help_text = """-Вопрос связанный со столовой? Напиши мне - “Столовая” или нажми на кнопку\n
-Появился запрос в СтудХ? Напиши мне - “Запрос” или нажми на кнопку\n
-Захотели оставить отзыв о работе СтудХ? Напиши мне - “Отзыв” или нажми на кнопку
"""

start_text = """Приветствую, дорогой ИОТовец!
Меня зовут Bot X. Я призван сделать нашe пространство более удобным для работы и отдыха. 
На данный момент, ты можешь обращаться ко мне по следующим вопросам: \n\n""" + help_text

error_text = 'Я вас не понимаю. Поробуйте воспользоваться кнопками или написать ключевые слова.\n\n' + help_text

replay_text_water = "Вот это ты молодец! Просто красавчик! Хоть когда-то в своей жизни не проебался."

request_text = "Напишите свой запрос:\n"

request_text_space = "Напишите свой запрос.\n" \
               "Пример запроса: \n\n" \
               "Иван Иванов 2 курс.\n" \
               "Нужно закупить расходники в 417. Готов всячески этому поспособствовать"

request_text_event = "Напишите свой запрос.\n" \
               "Пример запроса: \n\n" \
               "Иван Иванов 1 курс.\n" \
               "Я хотел бы провести турнир по Кс и Доте. Хотел бы получить помощь в оргонизации турника"

request_text_communication = "Напишите свой запрос.\n" \
               "Пример запроса: \n\n" \
               "Иван Иванов 3 курс.\n" \
               "Мне нужно получить служебную записку для выноса моего 3d принтера из корпуса."

answer_to_request = "Ваш запрос принят. В скором времени с вами свяжется представитель сферы."


answer_to_dining_room = "Уже заказываем. Спасибо за вклад в пространство."

