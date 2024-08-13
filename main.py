import telebot
import sqlite3


bot = telebot.TeleBot('7436759073:AAEn1HHjLmjzWEWaBy-hhzc1epSYS6PMrtw')
name = None

@bot.message_handler(commands=['start'])
def start(message):
    con = sqlite3.connect('basada.sql')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primiry key, name varcar(50), pass varcar(50))')
    con.commit()
    cur.close()
    con.close()


    bot.send_message(message.chat.id, 'Привет, все ок.Введите ваше имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name 
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Привет, все ок.ВВедите ваш пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    con = sqlite3.connect('basada.sql')
    cur = con.cursor()

    cur.execute("INSERT INTO users (name, pass), VALUES ('%s', '%s')" %(name, password))
    con.commit()
    cur.close()
    con.close()

    

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'сделано', reply_markup=markup)
    


bot.polling()