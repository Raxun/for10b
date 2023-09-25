import datetime
import telebot
from telebot import types
from data import db_session
from data.Сountries import User
from data.Сountries import Сountries
from data.Сountries import Niggers


bot = telebot.TeleBot('5512043516:AAEw192gJbRznPg60YLcqrubEcj9MY0WcHE', parse_mode=None)


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
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six,
                      User.Sev, User.Eig, User.Nin, User.Ten]
        elif int(datetime.datetime.today().weekday()) > int(sp_days.index(str(message.text)[0:-1])):
            if db_sess.query(Niggers.id).filter(Niggers.tag == message.from_user.username).first() is None:
                bot.send_message(message.chat.id, 'Если что, это расписание на следующую неделю😉')
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
        else:
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
    if (nums % 2) != 0:
        if datetime.datetime.today().weekday() != 6 and \
                int(datetime.datetime.today().weekday()) <= int(sp_days.index(str(message.text)[0:-1])):
            day = Сountries.Day
            sp_day = [Сountries.Fir, Сountries.Sec, Сountries.Thi, Сountries.For, Сountries.Fiv, Сountries.Six,
                      Сountries.Sev, Сountries.Eig, Сountries.Nin, Сountries.Ten]
        elif int(datetime.datetime.today().weekday()) > int(sp_days.index(str(message.text)[0:-1])):
            if db_sess.query(Niggers.id).filter(Niggers.tag == message.from_user.username).first() is None:
                bot.send_message(message.chat.id, 'Если что, это расписание на следующую неделю😉')
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six,
                      User.Sev, User.Eig, User.Nin, User.Ten]
        else:
            day = User.Day
            sp_day = [User.Fir, User.Sec, User.Thi, User.For, User.Fiv, User.Six,
                      User.Sev, User.Eig, User.Nin, User.Ten]
    sp2 = ['8:30', '9:20', '10:20', '11:20', '12:10', '13:00', '14:00', '15:00', '15:50', '16:40']
    for i in range(1, 9):
        lessons = db_sess.query(sp_day[i - 1]).filter(day == str(message.text)[0:-1]).first()
        sp.append(f"{i}.  {lessons[0]}")
    if db_sess.query(Niggers.id).filter(Niggers.tag == message.from_user.username).first() is not None:
        txt = db_sess.query(Niggers.text).filter(Niggers.tag == message.from_user.username).first()
        bot.send_message(message.chat.id, txt[0])
    else:
        bot.send_message(message.chat.id, '\n'.join(sp))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    db_session.global_init('db/Сountries.db')
    db_sess = db_session.create_session()
    if str(message.from_user.username) != 'Raxun':
        bot.send_message(1349592786, f"{'{0.first_name}'.format(message.from_user)},|{message.text},|"
                                     f"{message.from_user.username},| {message.chat.id}")
    if db_sess.query(Niggers.id).filter(Niggers.tag == message.from_user.username).first() is None:
        if message.text == 'Понедельник😭' and "@" not in message.text:
            raspisynie(message)
        elif message.text == 'Вторник☹' and "@" not in message.text:
            raspisynie(message)
        elif message.text == 'Среда🙁' and "@" not in message.text:
            raspisynie(message)
        elif message.text == 'Четверг😕' and "@" not in message.text:
            raspisynie(message)
        elif message.text == 'Пятница😐' and "@" not in message.text:
            raspisynie(message)
        elif message.text == 'Суббота🙂' and "@" not in message.text:
            raspisynie(message)
        elif message.text == 'Воскресенье🤩' and "@" not in message.text and \
                db_sess.query(Niggers.id).filter(Niggers.tag == message.from_user.username).first() is None:
            video = open('videoplayback.mp4', 'rb')
            bot.send_video(message.chat.id, video)
            bot.send_message(message.chat.id, 'Ты в ловушке! В воскресенье нет уроков!')
            bot.send_message(message.chat.id, 'Расскажу по секрету, здесь есть парочка интересных фишек, одна из них '
                                              'срабатывает при наличии "чу" или "че" в сообщении')
        elif 'ты' in str(message.text).lower() and '?' not in message.text and "@" not in message.text:
            bot.send_message(message.chat.id, text='Я???')
        elif 'да' == str(message.text).lower() and '?' not in message.text and "@" not in message.text:
            bot.send_message(message.chat.id, text='Пизда😡')
        elif '?' in message.text and "@" not in message.text:
            bot.send_message(message.chat.id, 'Хз')
        elif 'нахуй' in str(message.text).lower() or 'на хуй' in str(message.text).lower() and "@" not in message.text:
            bot.send_message(message.chat.id, 'Какой на хуй нахуй')
        elif str(message.text).lower().count('ы') >= 1 and "@" not in message.text:
            photo = open('IMG_20220920_094449_942.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif 'чу' in str(message.text).lower() or 'че' in str(message.text).lower() and "@" not in message.text:
            video = open('Aniche.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            if str(message.from_user.username) == 'Raxun' and "@" in message.text:
                texttt = message.text.split()
                if db_sess.query(Niggers.id).filter(Niggers.tag == texttt[0][1::]).first() is None:
                    try:
                        print(texttt[1])
                        s1 = Niggers()
                        s1.tag = texttt[0][1::]
                        s1.text = ' '.join(texttt[1::])
                        db_sess.add(s1)
                        db_sess.commit()
                        print(texttt[0][1::], ' '.join(texttt[1::]))
                        bot.send_message(message.chat.id, text="WELCUM NEW BEZDAR'")
                    except IndexError:
                        bot.send_message(message.chat.id, text='Введи текст долбабес')
                else:
                    delet = db_sess.query(Niggers).filter(Niggers.tag == texttt[0][1::]).first()
                    db_sess.delete(delet)
                    db_sess.commit()
                    bot.send_message(message.chat.id, text='Аутистик вылечился')
            else:
                bot.send_message(message.chat.id, 'Нет кнопок? Нажми > /start <')
    else:
        bot.send_message(message.chat.id,
                         db_sess.query(Niggers.text).filter(Niggers.tag == message.from_user.username).first()[0])


bot.polling(none_stop=True)