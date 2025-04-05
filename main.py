#-----------------------------БИБЛИОТЕКИ---------------------------------#
from email import message
import shutil
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
BOT_TOKEN = "7574653143:AAGjFy3nxp_Att6Iap_dnOT-M172xhlgL6M"

bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = 1646373003 # Основной администратор (Александр)
ADMIN_ID2 = 429952675 # Дополнительный администратор (Иван)

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
multipliers_file = "multipliers.json"

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
def get_eur_rub(): # Получаем курс от API Binance
    response1 = requests.get("https://alfabit.org/api/v1/cashe/operations/detail/%D0%A1%D0%B1%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA(RUB)/Tether(USDT)%20TRC20").json()
    products = response1["rate_data"]
    usd = float(products["value"])
    usd = round_if_zero(usd)
    #print(usd)

    response2 = requests.get("https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true").json()
    products = response2["data"]
    for product in products:
        if product["s"] == "EURUSDT":
            eur = float(product["c"])
            #print(eur)
            break

    return float(usd * eur)
    
def get_eur_rub_rate(type): # Подгоняем под нужный курс
    multipliers = load_multipliers() # загружаем множители из файла
    if type == "Покупка":
        eur_rub_buy = round_if_zero(round(get_eur_rub() * multipliers["buy"], 1))
        return eur_rub_buy 
    elif type == "Продажа":
        eur_rub_sell = round_if_zero(round(get_eur_rub() * multipliers["sell"], 1))
        return eur_rub_sell
    else:
        return None

def round_if_zero(x):
    # Получаем дробную часть числа
    frac = x - int(x)
    # Если дробная часть равна нулю, округляем число до целого
    if frac == 0:
        return int(round(x))
    # Иначе возвращаем исходное число
    else:
        return x

def load_multipliers(): #Загрузка множителя курса из файла
    try:
        with open(multipliers_file, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"buy": 1.055, "sell": 1}
    except json.JSONDecodeError:
        return {"buy": 1.055, "sell": 1}

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
def delete_user_info_about(message): # Чистка файлов
    try:
        with open("users_id.json", 'w') as file:
            data = {} # создаем пустой словарь
            json.dump(data, file) # сохраняем его в файл
        pass
    except:
        print("Файл users_id.json не был найден или не может быть открыт")
    try:
        with open("users_id_review.json", 'w') as file:
            data = {} # создаем пустой словарь
            json.dump(data, file) # сохраняем его в файл
    except:
        print("Файл users_id_review.json не был найден или не может быть открыт")
    try:
        with open("reviews.json", 'w') as file:
            data = {} # создаем пустой словарь
            json.dump(data, file) # сохраняем его в файл
    except:
        print("Файл reviews.json не был найден или не может быть открыт")
    try:
        with open("reviews_confirm.json", 'w') as file:
            data = {} # создаем пустой словарь
            json.dump(data, file) # сохраняем его в файл
    except:
        print("Файл reviews_confirm.json не был найден или не может быть открыт")
    
def delete_the_fucking_message(message): ####ЕБАННОЕ УДАЛЕНИЕ СООБЩЕНИЙ
    try:
        for i in range(1, 25):
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
    if user_state.user_id == ADMIN_ID:
        #print("Вы зашли как Администратор1")
        keyboard.add(types.InlineKeyboardButton('Обмен', callback_data='exchange'))
        keyboard.add(types.InlineKeyboardButton('Инструкция', callback_data='instructions'), types.InlineKeyboardButton('Отзывы', callback_data='reviews'))
        keyboard.add(types.InlineKeyboardButton('Курс', callback_data='rate'))
        keyboard.add(types.InlineKeyboardButton('Очистка файлов', callback_data='delete_all'), types.InlineKeyboardButton('Данные пользователей', callback_data='data'))
        keyboard.add(types.InlineKeyboardButton('Рез. Копирование', callback_data='backup'), types.InlineKeyboardButton('Восстановление', callback_data='restore'))
        keyboard.add(types.InlineKeyboardButton('Изменить курс', callback_data='change_rate'))
    elif user_state.user_id == ADMIN_ID2:
        #print("Вы зашли как Администратор2")
        keyboard.add(types.InlineKeyboardButton('Обмен', callback_data='exchange'))
        keyboard.add(types.InlineKeyboardButton('Инструкция', callback_data='instructions'), types.InlineKeyboardButton('Отзывы', callback_data='reviews'))
        keyboard.add(types.InlineKeyboardButton('Курс', callback_data='rate'))
        keyboard.add(types.InlineKeyboardButton('Изменить курс', callback_data='change_rate'))
    else:
        #print("Обычный пользователь зашёл в главное меню")
        keyboard.add(types.InlineKeyboardButton('Обмен', callback_data='exchange'))
        keyboard.add(types.InlineKeyboardButton('Инструкция', callback_data='instructions'), types.InlineKeyboardButton('Отзывы', callback_data='reviews'))
        keyboard.add(types.InlineKeyboardButton('Курс', callback_data='rate'))
 
    bot.send_message(message.chat.id, 'Добро пожаловать в сервис по обмену валют 💱\n', reply_markup=keyboard)

def rate(message):
    text_msg = "Загрузка курса⌛"
    msg = bot.send_message(message.chat.id, text_msg)

    delete_the_fucking_message(message) #####

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
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data='cancel'))

    text = "1. Подаёте заявку на обмен валюты через кнопку <b>«Обмен»</b> в главном меню бота, предварительно ознакомившись с курсом в соответствующем разделе. \nПотребуется предоставить следующую информацию:\n▪️Тип перевода (покупка/продажа)\n▪️Название банка, с которого будет осуществлён перевод\n▪️Сумма\n▪️Реквизиты вашей карты для зачисления средств\n\n2. В ближайшее время я свяжусь с вами для уточнения готовности выполнить перевод и предоставлю реквизиты для оплаты.\n\n3. После получения данных от меня, <b>в течение 15 минут</b>, следует отправить средства с указанием комментария к платежу, а также предоставить чек.\n\n4. Деньги поступят на указанные вами в заявке реквизиты в течение 30-60 минут.\n\n5. Как только деньги поступят на ваш счёт, необходимо <b>сразу</b> прислать скрин прихода средств."
    bot.send_message(message.chat.id, text, parse_mode='html' , reply_markup=keyboard)

    delete_the_fucking_message(message) #####

def reviews(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Написать отзыв', callback_data='write'), types.InlineKeyboardButton('Посмотреть отзывы', callback_data='read'))
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data='cancel'))

    bot.send_message(message.chat.id, "Вы можете оставить отзыв о моей работе или посмотреть отзывы пользователей", reply_markup=keyboard)
    delete_the_fucking_message(message)

def reviews_write(message):
    if check_user_id(message.chat.id) == False:
        bot.send_message(message.chat.id, "К сожалению, ты не можешь написать отзыв, так как ты ещё не оформил ни одной заявки. 😭")
        reviews(message)
    elif check_user_id_review(message.chat.id) == True:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('В главное меню', callback_data='cancel'))
        
        bot.send_message(message.chat.id, "Вы уже писали отзыв!", reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

        bot.send_message(message.chat.id, "Напиши свой отзыв о моей работе. Я буду рад услышать твое мнение. 😊", reply_markup=keyboard)
        bot.register_next_step_handler(message, confirm_check_reviews)

def confirm_check_reviews(message):
    text = message.text
    user_id = message.chat.id

    if user_id not in user_reviews:
        user_reviews[user_id] = []

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Опубликовать', callback_data=f'confirm_review_by_admin:{user_id}'), types.InlineKeyboardButton('Отклонить', callback_data=f'cancel_review_by_admin:{user_id}'))

    print("Отзыв отправил пользователь: ", user_id)

    user_reviews[user_id] = [f"✅ @{message.from_user.username}: {text}\n"]
    
    bot.send_message(ADMIN_ID2, f"Пользователь @{message.from_user.username} оставил свой отзыв: {text}", reply_markup=keyboard)

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('В главное меню', callback_data='cancel'))
    
    bot.send_message(message.chat.id, "Спасибо за ваш отзыв! 😊\n", reply_markup=keyboard)
    save_user_id_review(message.chat.id)
    save_reviews_confirm()

    delete_the_fucking_message(message)

def confirm_review_by_admin(call, user_id):
    user_reviews = load_reviews_confirm()
    review = user_reviews[user_id][0]
    save_reviews(user_id)
    delete_review_from_buffer(user_id)

    bot.send_message(call.message.chat.id, f"Отзыв пользователя @{bot.get_chat_member(user_id, user_id).user.username} был успешно опубликован! 🎉")

def cancel_review_by_admin(call, user_id):
    delete_review_from_buffer(user_id)
    print(check_user_id_review(user_id))

    bot.send_message(call.message.chat.id, f"Отзыв пользователя @{bot.get_chat_member(user_id, user_id).user.username} был успешно отклонён! 🎉")

def reviews_read(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Написать отзыв', callback_data='write'), types.InlineKeyboardButton('В главное меню', callback_data='cancel'))

    user_reviews = load_reviews()
    if user_reviews:
        reviews_text = ""
        for user_id, reviews in user_reviews.items():
            for review in reviews:
                reviews_text += f"{review}\n"
        bot.send_message(message.chat.id, f"Вот что пишут о моей работе пользователи:\n\n{reviews_text}", reply_markup=keyboard)
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

def amount_input(message): # ВВОД СУММЫ
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    bot.send_message(message.chat.id, 'Укажите сумму обмена в евро (минимум 100):', reply_markup=keyboard)

    delete_the_fucking_message(message) #####

    bot.register_next_step_handler(message, amount_check)

def amount_check(message): # ПРОВЕРКА СУММЫ
    try:
        amount = int(message.text)

        if amount >= 100 and amount <= 1000000:
            user_state.amount = amount
            #print("Пользователь ввёл сумму")
            iban_input(message)
        else:
            bot.send_message(message.chat.id, 'Сумма должна быть больше 100 евро. Попробуй еще раз.')
            amount_input(message)
    except:
        if message.text == '/start':
            delete_the_fucking_message(message) #####
            start_screen(message)
        else:
            bot.send_message(message.chat.id, 'Сумма должна быть числом. Попробуй еще раз.')
            amount_input(message)

def iban_input(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))  

    bot.send_message(message.chat.id, 'Укажите ваш IBAN:', reply_markup=keyboard)

    delete_the_fucking_message(message)

    bot.register_next_step_handler(message, iban_check)

def iban_check(message):
    if message.text == '/start':
        start_screen(message)
        delete_the_fucking_message(message)
    else:
        user_state.iban = message.text
        name_input(message)

def name_input(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    bot.send_message(message.chat.id, 'Ваши имя и фамилия латиницей:', reply_markup=keyboard)

    delete_the_fucking_message(message)
    
    bot.register_next_step_handler(message, name_check)

def name_check(message):
    if message.text == '/start':
        start_screen(message)
        delete_the_fucking_message(message)
    else:
        if re.match("^[A-Za-z ]+$", message.text):
            user_state.name = message.text
            confirm_screen(message)
        else:
            bot.send_message(message.chat.id, 'Пожалуйста, введите имя и фамилию латиницей без цифр и кириллицы.')
            name_input(message)

def confirm_screen(message): # ПРОЦЕСС ОКОНЧАТЕЛЬНОГО ОФОРМЛЕНИЯ ЗАЯВКИ
    #print("Пользователь оформил заявку")
    user_state.username = message.from_user.username
    user_state.user_id = message.chat.id
    #print(user_state.username)
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Подтвердить', callback_data='confirm'), types.InlineKeyboardButton('Отмена', callback_data='cancel'))

    if user_state.type == "Покупка":
        bot.send_message(message.chat.id, f'Подтвердите ваши данные:\n\nТип перевода: <b>{user_state.type}</b>\nВаш банк: <b>{user_state.bank}</b>\nОтдаёте: <b>{round_if_zero(user_state.amount * get_eur_rub_rate("Покупка"))} руб.</b>\nПолучаете: <b>{user_state.amount} евро</b>\nIBAN: <b>{user_state.iban}</b>\nИмя и Фамилия: <b>{user_state.name}</b>',
                        parse_mode='html', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, f'Подтвердите ваши данные:\n\nТип перевода: <b>{user_state.type}</b>\nВаш банк: <b>{user_state.bank}</b>\nОтдаёте: <b>{user_state.amount} евро</b>\nПолучаете: <b>{round_if_zero(user_state.amount * get_eur_rub_rate("Продажа"))} руб.</b>\nIBAN: <b>{user_state.iban}</b>\nИмя и Фамилия: <b>{user_state.name}</b>',
                        parse_mode='html', reply_markup=keyboard)
    delete_the_fucking_message(message)

def confirm_exit(message): # ПРОЦЕСС ПОДТВЕРЖДЕНИЯ ЗАЯВКИ И ОТПРАВКА ЕЁ АДМИНИСТРАТОРУ
    #print("Пользователь отправил заявку администраторам!")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('В главное меню', callback_data='cancel'))
    bot.send_message(message.chat.id, f"✅ Ваша заявка создана!\n\nОжидайте, в ближайшее время свяжусь с вами 📞", reply_markup=keyboard)

    if user_state.type == "Покупка":
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты от пользователя @{user_state.username}:\n\nТип перевода: {user_state.type}\nБанк: {user_state.bank}\nСумма обмена: {user_state.amount} EUR \nСумма обмена в рублях: {round_if_zero(user_state.amount * get_eur_rub_rate('Покупка'))} RUB\nIBAN: {user_state.iban}\nИмя и Фамилия: {user_state.name}\n\nСвяжитесь с пользователем по идентификатору @{user_state.username} для уточнения деталей обмена.")
        #bot.send_message(ADMIN_ID2, f"#заявка\n\nТип перевода: <b>{user_state.type}</b>\nБанк: <b>{user_state.bank}</b>\nСумма: <b>{user_state.amount} евро</b> (<b>{round_if_zero(user_state.amount * get_eur_rub_rate('Покупка'))} руб.</b>)\n\n<b>{user_state.iban}</b>\n<b>{user_state.name}</b>\n\n<b>@{user_state.username}</b>", parse_mode='html')
    else:
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты от пользователя @{user_state.username}:\n\nТип перевода: {user_state.type}\nБанк: {user_state.bank}\nСумма обмена: {user_state.amount} EUR \nСумма обмена в рублях: {round_if_zero(user_state.amount * get_eur_rub_rate('Продажа'))} RUB\nIBAN: {user_state.iban}\nИмя и Фамилия: {user_state.name}\n\nСвяжитесь с пользователем по идентификатору @{user_state.username} для уточнения деталей обмена.")
        #bot.send_message(ADMIN_ID2, f"#заявка\n\nТип перевода: <b>{user_state.type}</b>\nБанк: <b>{user_state.bank}</b>\nСумма: <b>{user_state.amount} евро</b> (<b>{round_if_zero(user_state.amount * get_eur_rub_rate('Продажа'))} руб.</b>)\n\n<b>{user_state.iban}</b>\n<b>{user_state.name}</b>\n\n<b>@{user_state.username}</b>", parse_mode='html')

    delete_the_fucking_message(message) #####
    
    save_user_id(user_state.user_id)

def show_data(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Назад', callback_data='cancel'))

    data_text = ""
    try:
        with open(userID_file, 'r') as file:
            data = json.load(file)
            user_ids = data.get('user_ids', [])
            if user_ids != []:
                for user_id in user_ids:
                    try:
                        with open(userID_file_review, 'r') as file:
                            data = json.load(file)
                            user_ids_review = data.get('user_ids', [])
                            if user_id in user_ids:
                                if user_id in user_ids_review:
                                    username = bot.get_chat_member(user_id, user_id).user.username
                                    data_text += f"@{username} - сделал заявку и оставил отзыв\n"
                                else:
                                    username = bot.get_chat_member(user_id, user_id).user.username
                                    data_text += f"@{username} - сделал заявку\n"
                    except FileNotFoundError:
                        return False
                    except Exception as e:
                        return False
                bot.send_message(message.chat.id, f"Вот данные о пользователях, которые сделали заявку и/или оставили отзыв:\n\n{data_text}", reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id, "Пока еще нет данных о пользователях. 😢", reply_markup=keyboard)
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
    delete_the_fucking_message(message) #####

@bot.message_handler(commands=['start'])
def start_command(message):
    start_screen(message)
    delete_the_fucking_message(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    if data == 'exchange':
        exchange_type(call.message)
        delete_the_fucking_message(call.message)
    elif data == 'rate':
        rate(call.message)
    elif data == 'instructions':
        instructions(call.message)

    elif data == 'Покупка' or data == 'Продажа':
        user_state.type = data
        bank_choice(call.message)
        delete_the_fucking_message(call.message)
    elif data == 'Тинькофф' or data == 'Сбербанк' or data == 'Райффайзен':
        user_state.bank = data
        amount_input(call.message)
    elif data == 'confirm':
        confirm_exit(call.message)

    elif data == 'reviews':
        reviews(call.message)
    elif data == 'write':
        reviews_write(call.message)
        delete_the_fucking_message(call.message) #####
    elif data == 'read':
        reviews_read(call.message)
        delete_the_fucking_message(call.message) #####

    elif data.startswith('confirm_review_by_admin:'):
        #print("Администратор одобрил отзыв")
        user_id = data.split(':')[1]
        print("Отзыв пользователя: ", user_id, " был принят!")
        confirm_review_by_admin(call, user_id)
    elif data.startswith('cancel_review_by_admin:'):
        #print("Администратор отклонил отзыв")
        user_id = data.split(':')[1]
        print("Отзыв пользователя: ", user_id, " был отклонён!")
        cancel_review_by_admin(call, user_id)
        
    elif data == 'delete_all':
        delete_user_info_about(call.message)
        bot.send_message(call.message.chat.id, "Очистка завершена!")
        start_screen(call.message)
        delete_the_fucking_message(call.message) #####

    elif data == 'data':
        #print("Администратор просматривает данные о пользователях")
        delete_the_fucking_message(call.message) #####
        show_data(call.message)

    elif data == 'backup':
        backup_files()
        bot.send_message(call.message.chat.id, "Копия создана")
        start_screen(call.message)
        delete_the_fucking_message(call.message) #####
    elif data == 'restore':
        restore_files()
        bot.send_message(call.message.chat.id, "Копия восстановлена")
        start_screen(call.message)
        delete_the_fucking_message(call.message) #####

    elif data == 'change_rate':
        change_rate(call.message)
        delete_the_fucking_message(call.message) #####
    elif data == 'change_buy':
        change_buy(call.message)
        delete_the_fucking_message(call.message) #####
    elif data == 'change_sell':
        change_sell(call.message)
        delete_the_fucking_message(call.message) #####
    elif data.startswith('apply_buy:'):
        multiplier = float(data.split(':')[1])
        apply_buy(call, multiplier)
        delete_the_fucking_message(call.message) #####
    elif data.startswith('apply_sell:'):
        multiplier = float(data.split(':')[1])
        apply_sell(call, multiplier)
        delete_the_fucking_message(call.message) #####

    elif data == 'cancel':
        #print("Пользователь перешёл в главное меню, нажав кнопку Отмена")
        start_screen(call.message)
        delete_the_fucking_message(call.message)

#------------------------------------------ОТЗЫВЫ-------------------------------# 
def save_reviews(user_id):
    with open(reviews_file, mode="r") as file:
        user_reviews = json.load(file)
    with open(reviews_file_confirm, mode="r") as file:
        user_reviews_confirm = json.load(file)
    review = user_reviews_confirm[user_id][0]
    user_reviews[user_id] = [review]
    with open(reviews_file, mode="w") as file:
        json.dump(user_reviews, file)
        
def save_reviews_confirm():
    with open(reviews_file_confirm, mode="w") as file:
        json.dump(user_reviews, file)

def load_reviews():
    try:
        with open(reviews_file, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    
def load_reviews_confirm():
    try:
        with open(reviews_file_confirm, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def delete_review_confirm(user_id):
    user_reviews = load_reviews_confirm()
    del user_reviews[user_id]
    save_reviews_confirm()

#----------------------СОХРАНЕНИЯ-И-УДАЛЕНИЕ-МЕТРИКИ------------------------------#
def save_user_id(user_id):
    try:
        with open(userID_file, 'r') as file:
            data = json.load(file)
            user_ids = data.get('user_ids', [])
        if user_id in user_ids:
            print('Пользователь уже ранее оставалял заявки')
        else:
            with open(userID_file, 'w') as file:
                user_ids.append(user_id)
                data = {'user_ids': user_ids}
                json.dump(data, file)
    except Exception as e:
        print(f'Ошибка при сохранении User ID: {e}')

def delete_user_id(user_id):
    try:
        with open(userID_file, 'r') as file:
            data = json.load(file)
            user_ids = data.get('user_ids', [])
        with open(userID_file, 'w') as file:
            user_ids.remove(user_id)
            data = {'user_ids': user_ids}
            json.dump(data, file)
    except Exception as e:
        print(f'Ошибка при удалении User ID: {e}')

def save_user_id_review(user_id):
    try:
        with open(userID_file_review, 'r') as file:
            data = json.load(file)
            user_ids = data.get('user_ids', [])
        if user_id in user_ids:
            print('Пользователь уже ранее оставалял отзыв')
        else:
            with open(userID_file_review, 'w') as file:
                user_ids.append(user_id)
                data = {'user_ids': user_ids}
                json.dump(data, file)
    except Exception as e:
        print(f'Ошибка при сохранении User ID: {e}')

def check_user_id(user_id):
    try:
        with open(userID_file, 'r') as file:
            data = json.load(file)
            user_ids = data.get('user_ids', [])
            if user_id in user_ids:
                return True
            else:
                return False
    except FileNotFoundError:
        return False
    except Exception as e:
        return False

def check_user_id_review(user_id):
    try:
        with open(userID_file_review, 'r') as file:
            data = json.load(file)
            user_ids = data.get('user_ids', [])
            if user_id in user_ids:
                return True
            else:
                return False
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f'Ошибка при проверке User ID: {e}')
        return False
    
def delete_review_from_buffer(user_id):
    with open(reviews_file_confirm, mode="r") as file:
        user_reviews = json.load(file)
    if user_id in user_reviews:
        del user_reviews[user_id]
        with open(reviews_file_confirm, mode="w") as file:
            json.dump(user_reviews, file)

def load_user_ids():
    try:
        with open(userID_file, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def load_user_ids_review():
    try:
        with open(userID_file_review, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def backup_files(): # Функция для создания резервной копии всех файлов
    files = [userID_file, userID_file_review, reviews_file, reviews_file_confirm] # Список файлов для копирования
    for file in files: # Для каждого файла в списке
        shutil.copy(file, f"backup/{file}") # Копируем файл в папку backup с тем же именем
    print("Резервная копия успешно создана!")

def restore_files(): # Функция для восстановления файлов из резервной копии
    files = [userID_file, userID_file_review, reviews_file, reviews_file_confirm] # Список файлов для копирования
    for file in files: # Для каждого файла в списке
        shutil.copy(f"backup/{file}", file) # Копируем файл из папки backup в исходную директорию с заменой
    print("Файлы успешно восстановлены!")

def save_multipliers(multipliers): # Сохраняем множители в файл
    with open(multipliers_file, mode="w") as file:
        json.dump(multipliers, file)

def change_rate(message):
    # Выводим текущие множители курса и предлагаем выбрать тип обмена для изменения
    multipliers = load_multipliers()
    eur_rub_buy_str = get_eur_rub_rate("Покупка")
    eur_rub_sell_str = get_eur_rub_rate("Продажа")

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Покупка', callback_data='change_buy'), types.InlineKeyboardButton('Продажа', callback_data='change_sell'))
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))
    bot.send_message(message.chat.id, f"Текущий курс:\n\n🟢 RUB ➜ EUR: <b>{eur_rub_buy_str}</b>    Множитель: <b>{multipliers['buy']}</b>\n🔴 EUR ➜ RUB: <b>{eur_rub_sell_str}</b>   Множитель: <b>{multipliers['sell']}</b>\n\nВыберите тип обмена, который хотите изменить:", parse_mode='html', reply_markup=keyboard)
    
# Добавляем новые функции для обработки нажатия на кнопки покупка и продажа в меню изменения курса
def change_buy(message):
    # Просим ввести новый множитель курса покупки и регистрируем следующий шаг
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))
    bot.send_message(message.chat.id, "Введите новый множитель курса покупки (например, 1.05):", reply_markup=keyboard)
    bot.register_next_step_handler(message, confirm_buy)

def change_sell(message):
    # Просим ввести новый множитель курса продажи и регистрируем следующий шаг
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Отмена', callback_data='cancel'))
    bot.send_message(message.chat.id, "Введите новый множитель курса продажи (например, 0.95):", reply_markup=keyboard)
    bot.register_next_step_handler(message, confirm_sell)

# Добавляем новые функции для подтверждения изменения множителей курса
def confirm_buy(message):
    # Проверяем корректность введенного значения и выводим новый курс покупки
    try:
        multiplier = float(message.text)
        if multiplier > 0 and multiplier < 10:
            new_rate = round_if_zero(round(get_eur_rub() * multiplier, 1))
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton('Применить', callback_data=f'apply_buy:{multiplier}'), types.InlineKeyboardButton('Назад', callback_data='change_rate'))
            bot.send_message(message.chat.id, f"Новый множитель: <b>{multiplier}</b>\n\nНовый курс покупки: <b>{new_rate}</b>", parse_mode='html', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, "Множитель должен быть положительным числом меньше 10. Попробуйте еще раз.")
            change_buy(message)
    except:
        bot.send_message(message.chat.id, "Множитель должен быть числом. Попробуйте еще раз.")
        change_buy(message)

def confirm_sell(message):
    # Проверяем корректность введенного значения и выводим новый курс продажи
    try:
        multiplier = float(message.text)
        if multiplier > 0 and multiplier < 10:
            new_rate = round_if_zero(round(get_eur_rub() * multiplier, 1))
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton('Применить', callback_data=f'apply_sell:{multiplier}'), types.InlineKeyboardButton('Назад', callback_data='change_rate'))
            bot.send_message(message.chat.id, f"Новый множитель: <b>{multiplier}</b>\n\nНовый курс продажи: <b>{new_rate}</b>", parse_mode='html', reply_markup=keyboard)
        else:
            bot.send_message(message.chat.id, "Множитель должен быть положительным числом меньше 10. Попробуйте еще раз.")
            change_sell(message)
    except:
        bot.send_message(message.chat.id, "Множитель должен быть числом. Попробуйте еще раз.")
        change_sell(message)

# Добавляем новые функции для применения изменения множителей курса
def apply_buy(call, multiplier):
    # Сохраняем новый множитель курса покупки в файл и выводим сообщение об успехе
    multipliers = load_multipliers()
    multipliers["buy"] = multiplier
    save_multipliers(multipliers)
    bot.send_message(call.message.chat.id, f"Новый множитель курса покупки успешно применен! 🎉\n\nТеперь курс покупки составляет <b>{round_if_zero(round(get_eur_rub() * multiplier, 1))}</b>", parse_mode='html')
    start_screen(call.message)

def apply_sell(call, multiplier):
    # Сохраняем новый множитель курса продажи в файл и выводим сообщение об успехе
    multipliers = load_multipliers()
    multipliers["sell"] = multiplier
    save_multipliers(multipliers)
    bot.send_message(call.message.chat.id, f"Новый множитель курса продажи успешно применен! 🎉\n\nТеперь курс продажи составляет <b>{round_if_zero(round(get_eur_rub() * multiplier, 1))}</b>", parse_mode='html')
    start_screen(call.message)

# -------------------------ЗАПУСК----------------------------
bot.polling()
# -----------------------------------------------------------
# RUS: Телеграмм Бот разработанный под оформление заявок на обмен валюты связанные с Рублём и Евро
# ENG: Telegram Bot developed for processing applications for currency exchange related to the Ruble and Euro
#
# version 1.5.2 (stable version with new rate from Binance, no canceling user_id in administration aborting review)
#                                                                                              09.01.2024 0:38 GMT+9
# Features: The collection of rate information has been redone: now the data is taken from two sites, first the dollar to ruble 
#   exchange rate from the alfabit.org platform, then this value is multiplied by the euro to dollar rate from the official Binance rate
#
# Bugs and problems: The user_id dont removed if administrastion abort review, dont disapearing message after review sending
#
# (C) 2024 Aleksander Samarin, Blagoveshchensk, Russia
# Powered by RSantila 
# email ssaannttiillaa@gmail.com
# telegram @RSantila
# ------------------------------------------------------------------------------------------------------------------