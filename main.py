import datetime
import telebot
from telebot import types
from data import db_session
from data.Users import User
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
                     text="Привет, {0.first_name}! Я помогу тебе быть в курсе расписания "
                          "уроков😉".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['фыаввфлолдфьвфатфлфйййёёёёрёиоолывсмальдкпфоявтмжыдкапкешугкшщцыжчюсмбюиьтаулцд'])
def raspisynie(message):
    sp_day = []
    nums = int(datetime.datetime.utcnow().isocalendar()[1])
    x = datetime.datetime.now()
    print(datetime.datetime.today().weekday())
    if (nums % 2) == 0:
        print("{0} Четное (числитель)".format(nums))
        if datetime.datetime.today().weekday() != 6:
            db_sess = 'db/Сountries.db'
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
        else:
            db_sess = 'db/User.db'
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six, User.Sev, User.Eig, User.Nin,
                      User.Ten]
    if (nums % 2) != 0:
        print("{0} Нечетное (знаменатель)".format(nums))
        if datetime.datetime.today().weekday() != 6:
            db_sess = 'db/User.db'
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six, User.Sev, User.Eig, User.Nin,
                      User.Ten]
        else:
            db_sess = 'db/Сountries.db'
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
    print(db_sess, sp_day, day)
    db_session.global_init(db_sess)
    db_sess = db_session.create_session()
    sp = []
    print(str(message.text)[0:-1])
    for i in range(1, 11):
        lessons = db_sess.query(sp_day[i - 1]).filter(day == str(message.text)[0:-1]).first()
        print(lessons)
        sp.append(f"{i}.  {lessons[0]}")
    print(sp)
    bot.send_message(message.chat.id, '\n'.join(sp))
    if datetime.datetime.today().weekday() == 6:
        bot.send_message(message.chat.id, 'Сегодня воскресенье, поэтому расписание показывается на следующую неделю😚')






@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Понедельник😭':
        raspisynie(message)
    if message.text == 'Вторник☹':
        raspisynie(message)
    if message.text == 'Среда🙁':
        raspisynie(message)
    if message.text == 'Четверг😕':
        raspisynie(message)
    if message.text == 'Пятница😐':
        raspisynie(message)
    if message.text == 'Суббота🙂':
        raspisynie(message)
    if message.text == 'Воскресенье🤩':
        video = open('videoplayback.mp4', 'rb')
        bot.send_video(message.chat.id, video)
        bot.send_message(message.chat.id, 'Ты в ловушке! В воскресенье нет уроков!')


bot.polling(none_stop=True)
