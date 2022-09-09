import datetime
import telebot
from telebot import types
from data import db_session
from data.Сountries import User
from data.Сountries import Сountries


bot = telebot.TeleBot('5512043516:AAGZovB98UKgdAI1r_ADlojURAsLZhl0BuQ', parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник😭")
    btn2 = types.KeyboardButton("Вторник☹")
    btn3 = types.KeyboardButton("Среда🙁")
    btn4 = types.KeyboardButton("Четверг😕")
    btn5 = types.KeyboardButton("Пятница😐")
    btn6 = types.KeyboardButton("Суббота🙂")
    btn7 = types.KeyboardButton("Воскресенье🤩")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я помогу тебе быть в курсе расписания"
                          "😉 \n© Raxun".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['фыаввфлолдфьвфатфлфйййёёёёрёиоолывсмальдкпфоявтмжыдкапкешугкшщцыжчюсмбюиьтаулцд'])
def raspisynie(message):
    db_session.global_init('db/Сountries.db')
    db_sess = db_session.create_session()
    sp_day = []
    sp = []
    sp_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    nums = int(datetime.datetime.utcnow().isocalendar()[1])
    x = datetime.datetime.now()
    if (nums % 2) == 0:
        if datetime.datetime.today().weekday() != 6 and \
                int(datetime.datetime.today().weekday()) <= int(sp_days.index(str(message.text)[0:-1])):
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
        elif int(datetime.datetime.today().weekday()) > int(sp_days.index(str(message.text)[0:-1])):
            bot.send_message(message.chat.id, 'Расписание на следующую неделю👉🏿👌🏿')
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six, User.Sev, User.Eig, User.Nin,
                      User.Ten]
        else:
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six, User.Sev, User.Eig, User.Nin,
                      User.Ten]
    if (nums % 2) != 0:
        if datetime.datetime.today().weekday() != 6 and \
                int(datetime.datetime.today().weekday()) <= int(sp_days.index(str(message.text)[0:-1])):
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six, User.Sev, User.Eig, User.Nin,
                      User.Ten]
        elif int(datetime.datetime.today().weekday()) > int(sp_days.index(str(message.text)[0:-1])):
            bot.send_message(message.chat.id, 'Расписание на следующую неделю👉🏿👌🏿')
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
        else:
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
    sp2 = ['8:30', '9:20', '10:20', '11:20', '12:10', '13:00', '14:00', '15:00', '15:50', '16:40']
    for i in range(1, 9):
        lessons = db_sess.query(sp_day[i - 1]).filter(day == str(message.text)[0:-1]).first()
        sp.append(f"{i}.  {lessons[0]}")
    bot.send_message(message.chat.id, '\n'.join(sp))
    if datetime.datetime.today().weekday() == 6:
        bot.send_message(message.chat.id, 'Расписание на следующую неделю👉🏿👌🏿')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print("{0.first_name}".format(message.from_user))
    print(message.text)
    print(message.from_user.username)
    if message.text == 'Понедельник😭':
        raspisynie(message)
    elif message.text == 'Вторник☹':
        raspisynie(message)
    elif message.text == 'Среда🙁':
        raspisynie(message)
    elif message.text == 'Четверг😕':
        raspisynie(message)
    elif message.text == 'Пятница😐':
        raspisynie(message)
    elif message.text == 'Суббота🙂':
        raspisynie(message)
    elif message.text == 'Воскресенье🤩':
        video = open('videoplayback.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        bot.send_message(message.chat.id, 'Ты в ловушке! В воскресенье нет уроков!')
    elif ('ты' in message.text or 'Ты' in message.text) and '?' not in message.text:
        bot.send_message(message.chat.id, text='Сам такой😡')
    elif '?' in message.text:
        bot.send_message(message.chat.id, 'Хз')
    elif 'нахуй' in message.text or 'на хуй' in message.text:
        bot.send_message(message.chat.id, 'Какой на хуй нахуй')
    elif'чу' in message.text or 'Чу' in message.text or 'че' in message.text or 'Че' in message.text:
        video = open('Aniche.mp4', 'rb')
        bot.send_video(message.chat.id, video)
    else:
        bot.send_message(message.chat.id, 'Ау, кнопки для кого?')


bot.polling(none_stop=True)
