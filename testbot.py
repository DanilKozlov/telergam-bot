import requests
import datetime
import telebot
from decimal import Decimal

import mysql.connector
from mysql.connector import Error

import dbworker

bot = telebot.TeleBot('1308356697:AAEOlwYX6QcEuO0sVPGVp1v1FQFxzTjeDwg')

keyboard_choose_day = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard_choose_day.row('Понедельник', 'Вторник', 'Среда',)
keyboard_choose_day.row('Четверг', 'Пятница')


# Начало диалога
# @bot.message_handler(commands=["start"])
# def cmd_start(message):
#     state = dbworker.get_current_state(message.chat.id)
#     if state == config.States.S_ENTER_NAME.value:
#         bot.send_message(message.chat.id, "Кажется, кто-то обещал отправить своё имя, но так и не сделал этого :( Жду...")
#     else:  # Под "остальным" понимаем состояние "0" - начало диалога
#         bot.send_message(message.chat.id, "Привет! Как я могу к тебе обращаться?")
#         dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# # По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
# @bot.message_handler(commands=["reset"])
# def cmd_reset(message):
#     bot.send_message(message.chat.id, "Что ж, начнём по-новой. Как тебя зовут?")
#     dbworker.set_state(message.chat.id, config.States.S_ENTER_NAME.value)


# @bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_ENTER_AGE.value)
# def user_entering_age(message):
#     # А вот тут сделаем проверку
#     if not message.text.isdigit():
#         # Состояние не меняем, поэтому только выводим сообщение об ошибке и ждём дальше
#         bot.send_message(message.chat.id, "Что-то не так, попробуй ещё раз!")
#         return
#     # На данном этапе мы уверены, что message.text можно преобразовать в число, поэтому ничем не рискуем
#     if int(message.text) < 5 or int(message.text) > 100:
#         bot.send_message(message.chat.id, "Какой-то странный возраст. Не верю! Отвечай честно.")
#         return
#     else:
#         # Возраст введён корректно, можно идти дальше
#         bot.send_message(message.chat.id, "Когда-то и мне было столько лет...эх... Впрочем, не будем отвлекаться. "
#                                           "Отправь мне какую-нибудь фотографию.")
#         dbworker.set_state(message.chat.id, config.States.S_SEND_PIC.value)


# @bot.message_handler(content_types=["photo"],
#                      func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.S_SEND_PIC.value)
# def user_sending_photo(message):
#     # То, что это фотография, мы уже проверили в хэндлере, никаких дополнительных действий не нужно.
#     bot.send_message(message.chat.id, "Отлично! Больше от тебя ничего не требуется. Если захочешь пообщаться снова - "
#                      "отправь команду /start.")
#     dbworker.set_state(message.chat.id, config.States.S_START.value)


# if __name__ == "__main__":
#     bot.infinity_polling()


 
nums = int(datetime.datetime.utcnow().isocalendar()[1])
x = datetime.datetime.now()
week = 0

if (nums % 2) != 0:
    week = 2
    #print("{0} Четное (числитель)".format(nums))
 
if (nums % 2) == 0:
    week = 1
    #print("{0} Нечетное (знаменатель)".format(nums))

def work_func(week,day_of_week,id_user):
    listA = []
    listA = dbworker.get_current_state(week,day_of_week)
    if not listA:
         bot.send_message(id_user,'Ура!!! Нет пар') 
    for l in listA:
        bot.send_message(id_user,l) 
    
    

@bot.message_handler(commands=['start'])  
def main(message):    
    bot.send_message(message.chat.id, 'Привет, выбери день на какой показать расписание',reply_markup=keyboard_choose_day)
    
 
@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.lower() == 'понедельник':
        #bot.send_message(message.chat.id, 'Вот расписание',reply_markup=keyboard_choose_day)
        work_func(week,1,message.chat.id)
        bot.send_message(message.chat.id, ':D',reply_markup=keyboard_choose_day)         
    elif message.text.lower() == 'вторник':
        #bot.send_message(message.chat.id, 'Вот расписание',reply_markup=keyboard_choose_day)
        work_func(week,2,message.chat.id)
        bot.send_message(message.chat.id, ':D',reply_markup=keyboard_choose_day)
    elif message.text.lower() == 'среда':
        #bot.send_message(message.chat.id, 'Вот расписание',reply_markup=keyboard_choose_day)
        work_func(week,3,message.chat.id)
        bot.send_message(message.chat.id, ':D',reply_markup=keyboard_choose_day)
    elif message.text.lower() == 'четверг':
        #bot.send_message(message.chat.id, 'Вот расписание',reply_markup=keyboard_choose_day)
        work_func(week,4,message.chat.id)
        bot.send_message(message.chat.id, ':D',reply_markup=keyboard_choose_day)
    elif message.text.lower() == 'пятница':
        #bot.send_message(message.chat.id, 'Вот расписание',reply_markup=keyboard_choose_day)
        work_func(week,5,message.chat.id)
        bot.send_message(message.chat.id, ':D',reply_markup=keyboard_choose_day)
    elif message.text.lower() == 'суббота' or message.text.lower() == 'воскресенье': 
        bot.send_message(message.chat.id, 'Расписание отсутствует',reply_markup=keyboard_choose_day)
    else: 
        bot.send_message(message.chat.id, 'Некорректный ввод',reply_markup=keyboard_choose_day)

if __name__ == "__main__":
    bot.infinity_polling()