#-----------------------------БИБЛИОТЕКИ---------------------------------#
from email import message
import requests
import telebot
import time
import json
import re
import os
from telebot import types
#---------------------------------ПРОКСИ----------------------------------#
#from telebot import apihelper
#apihelper.proxy = {'http':'http://127.0.0.1:3128'}
#-------------------------ГЛОБАЛЬНЫЕ-ПЕРЕМЕННЫЕ---------------------------#
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = 000000000 # Основной администратор
ADMIN_ID2 = 000000000 # Дополнительный администратор

admins = [ADMIN_ID, ADMIN_ID2]

def is_admin(user_id):
    return user_id in admins

class UserState:
    def __init__(self):
        self.user_id = None
        self.type = None
        self.amount = None
        self.name = None
        self.iban = None
        self.bank = None
        self.username = None

last_request_time = {}
user_reviews = {}
user_state = UserState()

userID_file = "users_id.json"
userID_file_review = "users_id_review.json"
reviews_file = "reviews.json"
reviews_file_confirm = "reviews_confirm.json"

#-------------------------СБРОС-ДАННЫХ-ПОЛЬЗОВАТЕЛЯ----------------------------#
def reset_user_state():
    user_state.user_id = None
    user_state.type = None
    user_state.amount = None
    user_state.name = None
    user_state.iban = None
    user_state.bank = None
    user_state.username = None

#-------------------------КУРС-----------------------------#
def get_eur_rub(): # Определяем функцию для получения курса евро к рублю с помощью API Центробанка России
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    if response.status_code == 200:
        data = response.json()
        eur_rub = data["Valute"]["EUR"]["Value"]
        return float(eur_rub)
    else:
        return None
    
def get_eur_rub_rate(type): # Подгоняем под нужный курс
    if type == "Покупка":
        eur_rub_buy = round(get_eur_rub() * 1.053, 2)
        return eur_rub_buy 
    elif type == "Продажа":
        eur_rub_sell = round(get_eur_rub() * 0.975, 2)
        return eur_rub_sell
    else:
        return None
#-------------------------СПАМ-----------------------------#
def check_spam(user_id):
    current_time = time.time()
    if user_id in last_request_time:
        previous_time = last_request_time[user_id]
        delta = current_time - previous_time
        if delta >= 30:
            return True
        else:
            return False
    else:
        return True
#-----------------------------------УДАЛЕНИЕ------------------------------------#
def delete_user_info_about(message):
    try:
        os.remove("users_id.json")
    except:
        print("Файл users_id.json не был создан, чтобы его удалять")
    try:
        os.remove("users_id_review.json")
    except:
        print("Файл users_id_review.json не был создан, чтобы его удалять")
    try:
        os.remove("reviews.json")
    except:
        print("Файл reviews.json не был создан, чтобы его удалять")
    try:
        os.remove("reviews_confirm.json")
    except:
        print("Файл reviews_confirm.json не был создан, чтобы его удалять")
    
def clean_message_history(message): # Функция для очистки истории сообщений
    try:
        for i in range(1, 101):
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
    except:
        print("Удаление: Гипер Перегрузка")
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except:
        print("Удаление: Перегрузка")

def send_and_delete(message, text): #не используется
    sent_message = bot.send_message(message.chat.id, text)
    time.sleep(5)
    bot.delete_message(message.chat.id, sent_message.message_id)

def start_screen(message):
    reset_user_state() # Сброс данных пользователя
    bot.clear_step_handler_by_chat_id(message.chat.id) # Очистка буфера сообщений
    user_state.user_id = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    if is_admin(user_state.user_id):
        print("Вы зашли как Администратор")
        keyboard.add(types.InlineKeyboardButton('Обмен', callback_data='exchange'))
        keyboard.add(types.InlineKeyboardButton('Инструкция', callback_data='instructions'), types.InlineKeyboardButton('Отзывы', callback_data='reviews'))
        keyboard.add(types.InlineKeyboardButton('Курс', callback_data='rate'))
        keyboard.add(types.InlineKeyboardButton('Очистка файлов', callback_data='delete_all'))
    else:
        print("Обычный пользователь зашёл в главное меню")
        keyboard.add(types.InlineKeyboardButton('Обмен', callback_data='exchange'))
        keyboard.add(types.InlineKeyboardButton('Инструкция', callback_data='instructions'), types.InlineKeyboardButton('Отзывы', callback_data='reviews'))
        keyboard.add(types.InlineKeyboardButton('Курс', callback_data='rate'))
 
    bot.send_message(message.chat.id, 'Добро пожаловать в сервис по обмену валют 💱\n', reply_markup=keyboard)

def rate(message):
    text_msg = "Загрузка курса⌛"
    msg = bot.send_message(message.chat.id, text_msg)

    clean_message_history(message)

    eur_rub_buy_str = get_eur_rub_rate("Покупка")
    eur_rub_sell_str = get_eur_rub_rate("Продажа")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data='cancel'))

    if eur_rub_buy_str and eur_rub_sell_str is not None:
         text_msg = f"💰 Курс на данный момент:\n\n🟢 RUB ➜ EUR: <b>{eur_rub_buy_str}</b>\n🔴 EUR ➜ RUB: <b>{eur_rub_sell_str}</b>"
    else:
        text_msg = "Извини, я не смог получить данные по курсу евро. 😢"

    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=text_msg, parse_mode='html', reply_markup=keyboard)

def instructions(message):
    clean_message_history(message)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data='cancel'))

    text = "1. Подаёте заявку на обмен валюты через кнопку <b>«Обмен»</b> в главном меню бота, предварительно ознакомившись с курсом в соответствующем разделе. \nПотребуется предоставить следующую информацию:\n▪️Тип перевода (покупка/продажа)\n▪️Название банка, с которого будет осуществлён перевод\n▪️Сумма\n▪️Реквизиты вашей карты для зачисления средств\n\n2. В ближайшее время я свяжусь с вами для уточнения курса и готовности выполнить перевод. А также предоставлю реквизиты для оплаты.\n\n3. После получения реквизитов, <b>в течение 15 минут</b>, следует отправить средства с указанием комментария к платежу, а также предоставить чек.\n\n4. Деньги поступят на указанные вами в заявке реквизиты в течение 30-60 минут.\n\n5. Как только деньги поступят на ваш счёт, необходимо <b>сразу</b> прислать скрин прихода средств."
    bot.send_message(message.chat.id, text, parse_mode='html' , reply_markup=keyboard)

def reviews(message):
    clean_message_history(message)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Написать отзыв', callback_data='write'), types.InlineKeyboardButton('Просмотреть отзывы', callback_data='read'))
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data='cancel'))

    bot.send_message(message.chat.id, "Вы можете оставить отзыв о моей работе или посмотреть отзывы других пользователей", reply_markup=keyboard)

def reviews_write(message):
    if check_user_id(message.chat.id) == False:
        bot.send_message(message.chat.id, "К сожалению, ты не можешь написать отзыв, так как ты ещё не оформил ни одной заявки. 😭")
        reviews(message)
    elif check_user_id_review(message.chat.id) == True:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('В главное меню', callback_data='cancel'))
        
        bot.send_message(message.chat.id, "Вы уже писали отзыв!", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Напиши свой отзыв о моей работе. Я буду рад услышать твое мнение. 😊")
        bot.register_next_step_handler(message, confirm_check_reviews)

def confirm_check_reviews(message):
    text = message.text
    user_id = message.chat.id
    if user_id not in user_reviews:
        user_reviews[user_id] = []

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Опубликовать', callback_data='confirm_review_by_admin'))
    user_reviews[user_id] = [f"✅ @{message.from_user.username}: {text}\n"]
    
    bot.send_message(ADMIN_ID, f"Пользователь @{message.from_user.username} оставил свой отзыв: {text}", reply_markup=keyboard)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('В главное меню', callback_data='cancel'))
    
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв! 😊\n", reply_markup=keyboard)
    save_user_id_review(message.chat.id)

    clean_message_history(message)

def reviews_read(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Написать отзыв', callback_data='write'), types.InlineKeyboardButton('В главное меню', callback_data='cancel'))

    user_reviews = load_reviews()
    if user_reviews:
        reviews_text = ""
        for user_id, reviews in user_reviews.items():
            for review in reviews:
                reviews_text += f"{review}\n"
        bot.send_message(message.chat.id, f"Вот что пишут о моей работе другие пользователи:\n\n{reviews_text}", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Пока еще нет ни одного отзыва о моей работе. 😢", reply_markup=keyboard)
    
def exchange_type(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Покупка', callback_data='Покупка'), types.InlineKeyboardButton('Продажа', callback_data='Продажа'))
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    bot.send_message(message.chat.id, 'Хотите купить или продать евро?', reply_markup=keyboard)

def bank_choice(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Сбербанк', callback_data='Сбербанк'), types.InlineKeyboardButton('Тинькофф', callback_data='Тинькофф'), types.InlineKeyboardButton('Райффайзен', callback_data='Райффайзен'))
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    bot.send_message(message.chat.id, 'Укажите название банка, с которого будет осуществлён перевод:', reply_markup=keyboard)

def amount_input(message):
    clean_message_history(message)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    if user_state.type == 'Покупка':
        bot.send_message(message.chat.id, 'Укажите сумму обмена в рублях (минимум 10000):', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Укажите сумму обмена в евро (минимум 100):', reply_markup=keyboard)

    bot.register_next_step_handler(message, amount_check)

def amount_check(message):
    try:
        amount = int(message.text)
        if user_state.type == 'Покупка':
            if amount >= 10000 and amount <= 100000000:
                user_state.amount = amount
                iban_input(message)
            else:
                bot.send_message(message.chat.id, 'Сумма должна быть больше 10000 рублей. Попробуй еще раз.')
                amount_input(message)
        else:
            if amount >= 100 and amount <= 1000000:
                user_state.amount = amount
                iban_input(message)
            else:
                bot.send_message(message.chat.id, 'Сумма должна быть больше 100 евро. Попробуй еще раз.')
                amount_input(message)
    except:
        if message.text == '/start':
            clean_message_history(message)
            start_screen(message)
        else:
            bot.send_message(message.chat.id, 'Сумма должна быть числом. Попробуй еще раз.')
            amount_input(message)

def iban_input(message):
    clean_message_history(message)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))  

    bot.send_message(message.chat.id, 'Укажите ваш IBAN:', reply_markup=keyboard)

    bot.register_next_step_handler(message, iban_check)

def iban_check(message):
    if message.text == '/start':
        clean_message_history(message)
        start_screen(message)
    else:
        user_state.iban = message.text
        name_input(message)

def name_input(message):
    clean_message_history(message)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    bot.send_message(message.chat.id, 'Ваши имя и фамилия латиницей:', reply_markup=keyboard)

    bot.register_next_step_handler(message, name_check)

def name_check(message):
    if message.text == '/start':
        clean_message_history(message)
        start_screen(message)
    else:
        if re.match("^[A-Za-z ]+$", message.text):
            user_state.name = message.text
            confirm_screen(message)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите имя и фамилию латиницей без цифр и кириллицы.')
            name_input(message)

def confirm_exit(message):
    clean_message_history(message)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('В главное меню', callback_data='cancel'))
    bot.send_message(message.chat.id, f"✅ Ваша заявка создана!\n\nОжидайте, в ближайшее время свяжусь с вами 📞", reply_markup=keyboard)

    if user_state.type == "Покупка":
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты от пользователя @{user_state.username}:\n\nТип перевода: {user_state.type}\nБанк: {user_state.bank}\nСумма обмена: {user_state.amount} RUB\nIBAN: {user_state.iban}\nИмя и Фамилия: {user_state.name}\n\nСвяжитесь с пользователем по идентификатору @{user_state.username} для уточнения деталей обмена.")
    else:
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты от пользователя @{user_state.username}:\n\nТип перевода: {user_state.type}\nБанк: {user_state.bank}\nСумма обмена: {user_state.amount} EUR\nIBAN: {user_state.iban}\nИмя и Фамилия: {user_state.name}\n\nСвяжитесь с пользователем по идентификатору @{user_state.username} для уточнения деталей обмена.")

    save_user_id(user_state.user_id)
    print(user_state.user_id)

def confirm_screen(message):
    user_state.username = message.from_user.username
    print(user_state.username)
    clean_message_history(message)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Подтвердить', callback_data='confirm'), types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    if user_state.type == "Покупка":
        bot.send_message(message.chat.id, f'Подтвердите ваши данные:\n\nТип перевода: <b>{user_state.type}</b>\nВаш банк: <b>{user_state.bank}</b>\nСумма: <b>{user_state.amount} руб.</b>\nIBAN: <b>{user_state.iban}</b>\nИмя и Фамилия: <b>{user_state.name}</b>',
                        parse_mode='html', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, f'Подтвердите ваши данные:\n\nТип перевода: <b>{user_state.type}</b>\nВаш банк: <b>{user_state.bank}</b>\nСумма: <b>{user_state.amount} евро</b>\nIBAN: <b>{user_state.iban}</b>\nИмя и Фамилия: <b>{user_state.name}</b>',
                        parse_mode='html', reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start_command(message):
    start_screen(message)
    clean_message_history(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    if data == 'exchange':
        last_request_time[user_state.user_id] = time.time()
        exchange_type(call.message)
        clean_message_history(call.message)
    elif data == 'rate':
        rate(call.message)

    elif data == 'instructions':
        instructions(call.message)

    elif data == 'Покупка' or data == 'Продажа':
        user_state.type = data
        bank_choice(call.message)
        clean_message_history(call.message)
    elif data == 'Тинькофф' or data == 'Сбербанк' or data == 'Райффайзен':
        user_state.bank = data
        amount_input(call.message)

    elif data == 'confirm':
        confirm_exit(call.message)

    elif data == 'reviews':
        reviews(call.message)
    elif data == 'write':
        reviews_write(call.message)
        clean_message_history(call.message)
    elif data == 'read':
        reviews_read(call.message)
        clean_message_history(call.message)

    elif data == 'confirm_review_by_admin':
        save_reviews(message)

    elif data == 'delete_all':
        delete_user_info_about(call.message)
        bot.send_message(call.message.chat.id, "Очистка завершена!")

    elif data == 'cancel':
        clean_message_history(call.message)
        start_screen(call.message)

@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_review'))
def callback_delete_review(call):
    delete_review(call)

#------------------------------------------ОТЗЫВЫ-------------------------------# 
def save_reviews():
    with open(reviews_file, mode="w") as file:
        json.dump(user_reviews, file)
        
def load_reviews():
    try:
        with open(reviews_file, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
#----------------------СОХРАНЕНИЯ-И-УДАЛЕНИЕ-МЕТРИКИ------------------------------#
def save_user_id(user_id):
    try:
        with open(userID_file, 'w') as file:
            data = {'user_id': user_id}
            json.dump(data, file)
        print(f'User ID {user_id} успешно сохранен в файл {userID_file}')
    except Exception as e:
        print(f'Ошибка при сохранении User ID: {e}')
def delete_user_id(user_id):
    try:
        with open(userID_file, 'r') as file:
            data = json.load(file)
            user_id = data['user_id']
        with open(userID_file, 'w') as file:
            data = {}
            json.dump(data, file)
        print(f'User ID {user_id} успешно удален из файла {userID_file}')
    except Exception as e:
        print(f'Ошибка при удалении User ID: {e}')

def save_user_id_review(user_id):
    try:
        with open(userID_file_review, 'w') as file:
            data = {'user_id': user_id}
            json.dump(data, file)
        print(f'User ID {user_id} успешно сохранен в файл {userID_file_review}')
    except Exception as e:
        print(f'Ошибка при сохранении User ID: {e}')

def check_user_id(user_id):
    try:
        with open(userID_file, 'r') as file:
            data = json.load(file)
            if 'user_id' in data and data['user_id'] == user_id:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f'Файл {userID_file} не найден')
        return False
    except Exception as e:
        print(f'Ошибка при проверке User ID: {e}')
        return False
def check_user_id_review(user_id):
    try:
        with open(userID_file_review, 'r') as file:
            data = json.load(file)
            if 'user_id' in data and data['user_id'] == user_id:
                return True
            else:
                return False
    except FileNotFoundError:
        print(f'Файл {userID_file_review} не найден')
        return False
    except Exception as e:
        print(f'Ошибка при проверке User ID: {e}')
        return False

# -------------------------ЗАПУСК----------------------------
bot.polling()
# -----------------------------------------------------------
# Телеграмм Бот разработанный под оформление заявок на обмен валюты связанные с Рублём и Евро
# version 3.2 (stable version - added admin review approval system and increased transaction limits)
# -----------------------------------------------------------