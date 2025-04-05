#-----------------------БИБЛИОТЕКИ---------------------------#
import requests
import telebot
import time
import json
from telebot import types
#--------------------ГЛОБАЛЬНЫЕ-ПЕРЕМЕННЫЕ-------------------#
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_ID = 000000000 # Основной администратор
ADMIN_ID2 = 000000000 # Дополнительный администратор

admins = [ADMIN_ID]

def is_admin(user_id):
    return user_id in admins

last_request_time = {}
userID_file = "users_id.json"
userID_file_review = "users_id_review.json"
reviews_file = "reviews.json"
user_reviews = {}
#-------------------------ДАННЫЕ-ПОЛЬЗОВАТЕЛЯ-----------------#
class UserState:
    def __init__(self):
        self.user_id = None
        self.type = None
        self.amount = None
        self.name = None
        self.iban = None
        self.bank = None
        
user_state = UserState()
#-------------------------КУРС-----------------------------#
def get_eur_rub(): # Определяем функцию для получения курса евро к рублю с помощью API Центробанка России
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    if response.status_code == 200:
        data = response.json()
        # Извлекаем курс евро к рублю из словаря
        eur_rub = data["Valute"]["EUR"]["Value"]
        # Возвращаем курс в виде числа с плавающей точкой
        return float(eur_rub)
    else:
        return None
    
def get_eur_rub_rate(type): # Преобразуемый полученные данные и подговняем под нужный курс
    if type == "Покупка":
        eur_rub_buy = round(get_eur_rub() * 1.053, 2)
        return eur_rub_buy 
    elif type == "Продажа":
        eur_rub_sell = round(get_eur_rub() * 0.975, 2)
        return eur_rub_sell
    else:
        return None
#-------------------------СПАМ-----------------------------#
def check_spam(user_id): # Определяем функцию для проверки, что пользователь не отправляет заявку слишком часто
    # Получаем текущее время в секундах с помощью модуля time
    current_time = time.time()
    # Проверяем, есть ли идентификатор пользователя в словаре last_request_time
    if user_id in last_request_time:
        # Если есть, получаем время его последней заявки
        previous_time = last_request_time[user_id]
        # Вычисляем разницу между текущим и предыдущим временем в секундах
        delta = current_time - previous_time
        # Проверяем, что разница больше или равна 120 секундам (2 минутам)
        if delta >= 120:
            return True
        else:
            return False
    else:
        return True
#-------------------------КЛАВИАТУРЫ-И-КНОПКИ-----------------------------#
    
def create_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса InlineKeyboardMarkup
    keyboard = types.InlineKeyboardMarkup()
    # Создаем три кнопки с помощью класса InlineKeyboardButton и текстом "Курс", "Инструкция" и "Обмен"
    button_rate = types.InlineKeyboardButton("Курс", callback_data="rate")
    button_instruction = types.InlineKeyboardButton("Инструкция", callback_data="instruction")
    # Создаем кнопку обмена с помощью класса InlineKeyboardButton и текстом "Обмен"
    button_exchange = types.InlineKeyboardButton("Обмен", callback_data="exchange")
    button_reviews = types.InlineKeyboardButton("Отзывы", callback_data="reviews")
    # Добавляем кнопку обмена на клавиатуру в новый ряд с помощью метода row
    keyboard.row(button_exchange)
    # Добавляем кнопки на клавиатуру в один ряд с помощью метода add
    keyboard.add(button_rate, button_instruction)
    # Добавляем кнопку обмена на клавиатуру в новый ряд с помощью метода row
    keyboard.row(button_reviews)
    # Возвращаем клавиатуру
    return keyboard

def create_type_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса ReplyKeyboardMarkup
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем две кнопки с помощью класса KeyboardButton и текстом "Покупка" и "Продажа"
    button_buy = types.KeyboardButton("Покупка")
    button_sell = types.KeyboardButton("Продажа")
    # Добавляем кнопки на клавиатуру в один ряд с помощью метода add
    keyboard.add(button_buy, button_sell)
    # Возвращаем клавиатуру
    return keyboard

def create_bank_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса ReplyKeyboardMarkup
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем три кнопки с помощью класса KeyboardButton и текстом "Тинькофф", "Сбербанк" и "Альфабанк"
    button_tinkoff = types.KeyboardButton("Сбербанк")
    button_sberbank = types.KeyboardButton("Тинькофф")
    button_alfabank = types.KeyboardButton("Райффайзен")
    # Добавляем кнопки на клавиатуру в один ряд с помощью метода add
    keyboard.add(button_tinkoff, button_sberbank, button_alfabank)
    # Возвращаем клавиатуру
    return keyboard

def create_cancel():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_cancel = types.KeyboardButton("Отмена")
    # Добавляем кнопки на клавиатуру в один ряд с помощью метода add
    keyboard.add(button_cancel)
    # Возвращаем клавиатуру
    return keyboard

def create_confirm_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса ReplyKeyboardMarkup
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем две кнопки с помощью класса KeyboardButton и текстом "Подтвердить" и "Отмена"
    button_confirm = types.KeyboardButton("Подтвердить")
    button_cancel = types.KeyboardButton("Отмена")
    # Добавляем кнопки на клавиатуру в один ряд с помощью метода add
    keyboard.add(button_confirm, button_cancel)
    # Возвращаем клавиатуру
    return keyboard

def create_review_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса ReplyKeyboardMarkup
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_write = types.KeyboardButton("Написать отзыв")
    button_view = types.KeyboardButton("Просмотреть отзывы")
    button_cancel = types.KeyboardButton("Отмена")
    keyboard.add(button_write, button_view, button_cancel)
    # Возвращаем клавиатуру
    return keyboard

#----------------------------ОБРАБОТЧИКИ------------------------------#

@bot.message_handler(commands=["start"])
def start(message):
    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, f"Здравствуйте, {message.from_user.first_name}! Вы администратор этого бота. Что вы хотите сделать?")
    else:
        bot.send_message(message.chat.id, "Я могу помочь тебе купить или продать евро по выгодному курсу. 💶", reply_markup=create_keyboard())

@bot.message_handler(commands=["rate"])
def rate(message):
    eur_rub_buy_str =  get_eur_rub_rate("Покупка")
    eur_rub_sell_str =  get_eur_rub_rate("Продажа")
    if eur_rub_buy_str and eur_rub_sell_str is not None:
        text = f"💰 Курс на данный момент:\n\n🟢 RUB ➜ EUR: <b>{eur_rub_buy_str}</b>\n🔴 EUR ➜ RUB: <b>{eur_rub_sell_str}</b>"
        # Отправляем сообщение пользователю с помощью метода send_message
        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=create_keyboard())
    else:
        text = "Извини, я не смог получить данные по курсу евро. 😢\nПопробуй позже или напиши мне /start, чтобы узнать, что я умею."
        # Отправляем сообщение пользователю с извинением и эмодзи
        bot.send_message(message.chat.id, text, reply_markup=create_keyboard())

@bot.message_handler(commands=["instruction"])
def instruction(message):
    # Составляем текст сообщения с инструкцией и эмодзи
    text = "1. Подаёте заявку на обмен валюты через кнопку <b>«Обмен»</b> в главном меню бота, предварительно ознакомившись с курсом в соответствующем разделе. \nПотребуется предоставить следующую информацию:\n▪️Тип перевода (покупка/продажа)\n▪️Название банка, с которого будет осуществлён перевод\n▪️Сумма\n▪️Реквизиты вашей карты для зачисления средств\n\n2. В ближайшее время я свяжусь с вами для уточнения курса и готовности выполнить перевод. А также предоставлю реквизиты для оплаты.\n\n3. После получения реквизитов, <b>в течение 15 минут</b>, следует отправить средства с указанием комментария к платежу, а также предоставить чек.\n\n4. Деньги поступят на указанные вами в заявке реквизиты в течение 30-60 минут.\n\n5. Как только деньги поступят на ваш счёт, необходимо <b>сразу</b> прислать скрин прихода средств."
    # Отправляем сообщение пользователю с помощью метода send_message
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=create_keyboard())

@bot.message_handler(commands=["exchange"])
def exchange(message):
    # Сохраняем идентификатор пользователя в атрибут user_id объекта user_state
    user_state.user_id = message.chat.id
    if check_spam(user_state.user_id):
        # Если не спамит, то обновляем время его последней заявки в словаре last_request_time
        last_request_time[user_state.user_id] = time.time()
        # Отправляем сообщение пользователю с вопросом о типе перевода (покупка или продажа евро) и двумя кнопками "Покупка" и "Продажа"
        bot.send_message(message.chat.id, "Ты хочешь купить или продать евро?", reply_markup=create_type_keyboard())
        # Переводим пользователя в режим ожидания ответа на вопрос о типе перевода
        print(message)
        bot.register_next_step_handler(message, process_type_step)
    else:
        # Если спамит, то отправляем сообщение пользователю с предупреждением и эмодзи
        bot.send_message(message.chat.id, "Ты отправляешь заявки слишком часто! 😡\nПодожди две минуты перед следующей заявкой.")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    # Получаем данные от кнопки, на которую нажал пользователь
    data = call.data
    # Проверяем, что данные соответствуют одному из вариантов
    if data == "rate":
        # Если данные равны "rate", вызываем функцию rate, которая выводит курс евро к рублю и добавляет к нему по 6 процентов
        rate(call.message)
    elif data == "instruction":
        # Если данные равны "instruction", вызываем функцию instruction, которая выводит инструкцию по обмену валюты через бота
        instruction(call.message)
    elif data == "exchange":
        # Если данные равны "instruction", вызываем функцию instruction, которая выводит инструкцию по обмену валюты через бота
        exchange(call.message)
    elif data == "reviews":
        # Если данные равны "instruction", вызываем функцию instruction, которая выводит инструкцию по обмену валюты через бота
        reviews(call.message)
#-----------------------------------ОФОРМЛЕНИЕ-ЗАЯВКИ---------------------------------#
def process_type_step(message):
    # Получаем текст сообщения пользователя
    text = message.text
    # Проверяем, что текст соответствует одному из вариантов
    if text == "Покупка" or text == "Продажа":
        user_state.type = text
        #eur_rub = get_eur_rub_rate(user_state.type)
        bot.send_message(message.chat.id, f"{user_state.type} евро. 💶\nВведите сумму в евро, которую ты хочешь купить.\nНапиши число без знаков и пробелов. Например: 123", reply_markup=create_cancel())
        # Переводим пользователя в режим ожидания ответа на вопрос о сумме обмена
        bot.register_next_step_handler(message, process_amount_step)
    else:
        # Если текст не соответствует одному из вариантов, отправляем сообщение пользователю с просьбой выбрать одну из кнопок на клавиатуре
        bot.send_message(message.chat.id, "Пожалуйста, выбери одну из опций на клавиатуре: Покупка или Продажа.", reply_markup=create_cancel())
        # Переводим пользователя в режим ожидания ответа на вопрос о типе перевода
        bot.register_next_step_handler(message, process_type_step)

def process_amount_step(message):
    # Получаем текст сообщения пользователя
    text = message.text
    # Проверяем, что текст является числом
    try:
        # Преобразуем текст в число с плавающей точкой
        amount = float(text)
        # Проверяем, что число положительное и не равно нулю
        if amount > 0:
            # Если число положительное и не равно нулю, сохраняем его в атрибут amount объекта user_state
            user_state.amount = amount
            # Отправляем сообщение пользователю с вопросом о его имени и фамилии
            bot.send_message(message.chat.id, "Как тебя зовут? Напиши свое имя и фамилию.", reply_markup=create_cancel())
            # Переводим пользователя в режим ожидания ответа на вопрос о имени и фамилии
            bot.register_next_step_handler(message, process_name_step)
        else:
            # Если число отрицательное или равно нулю, отправляем сообщение пользователю с просьбой ввести положительное число
            bot.send_message(message.chat.id, "Пожалуйста, введи положительное число больше нуля.", reply_markup=create_cancel())
            # Переводим пользователя в режим ожидания ответа на вопрос о сумме обмена
            bot.register_next_step_handler(message, process_amount_step)
    except ValueError:
        # Если текст не является числом, отправляем сообщение пользователю с просьбой ввести число без знаков и пробелов
        bot.send_message(message.chat.id, "Пожалуйста, введи число без знаков и пробелов. Например: 1000", reply_markup=create_cancel())
        # Переводим пользователя в режим ожидания ответа на вопрос о сумме обмена
        bot.register_next_step_handler(message, process_amount_step)

def process_name_step(message):
    # Получаем текст сообщения пользователя
    text = message.text
    # Сохраняем текст в атрибут name объекта user_state
    user_state.name = text
    # Отправляем сообщение пользователю с вопросом о его IBAN (международном номере банковского счета)
    bot.send_message(message.chat.id, "Какой у тебя IBAN? Напиши свой международный номер банковского счета без пробелов. Например: AU12345678901234567890", reply_markup=create_cancel())
    # Переводим пользователя в режим ожидания ответа на вопрос о IBAN
    bot.register_next_step_handler(message, process_iban_step)

def process_iban_step(message):
    # Получаем текст сообщения пользователя
    text = message.text
    # Сохраняем текст в атрибут iban объекта user_state
    user_state.iban = text
    # Отправляем сообщение пользователю с подтверждением его заявки и кнопкой "Подтвердить"
    bot.send_message(message.chat.id, "Пожалуйста, выбери один из трех банков на клавиатуре: Тинькофф, Сбербанк или Альфабанк.", reply_markup=create_bank_keyboard())    # Переводим пользователя в режим ожидания ответа на подтверждение заявки
    bot.register_next_step_handler(message, process_bank_step)

def process_bank_step(message):
    # Получаем текст сообщения пользователя
    text = message.text
    # Проверяем, что текст соответствует одному из вариантов
    if text == "Сбербанк" or text == "Тинькофф" or text == "Райффайзен":
        # Если текст равен одному из вариантов, сохраняем его в атрибут bank объекта user_state
        user_state.bank = text
        # Отправляем сообщение пользователю с подтверждением его заявки и кнопкой "Подтвердить"
        bot.send_message(message.chat.id, f"Твоя заявка на обмен валюты:\n\nТип перевода: {user_state.type}\nСумма обмена: {user_state.amount} евро\nИмя и фамилия: {user_state.name}\nIBAN: {user_state.iban}\nБанк: {user_state.bank}\n\nЕсли все верно, нажми кнопку Подтвердить.", reply_markup=create_confirm_keyboard())
        # Переводим пользователя в режим ожидания ответа на подтверждение заявки
        bot.register_next_step_handler(message, process_confirm_step)
    else:
        # Если текст не соответствует одному из вариантов, отправляем сообщение пользователю с просьбой выбрать одну из кнопок на клавиатуре
        bot.send_message(message.chat.id, "Пожалуйста, выбери один из трех банков на клавиатуре: Тинькофф, Сбербанк или Альфабанк.")
        # Переводим пользователя в режим ожидания ответа на вопрос о выборе банка
        bot.register_next_step_handler(message, process_bank_step)

def process_confirm_step(message):
    # Получаем текст сообщения пользователя 
    text = message.text
    # Проверяем, что текст равен "Подтвердить"
    if text == "Подтвердить":
        # Если текст равен "Подтвердить", отправляем сообщение пользователю с благодарностью и информацией о том, что его заявка отправлена администратору бота
        bot.send_message(message.chat.id, "Спасибо за твою заявку! 🙏\nЯ отправил ее администратору бота, и он скоро свяжется с тобой для уточнения деталей обмена. 📞", reply_markup=types.ReplyKeyboardRemove())
        # Отправляем сообщение администратору бота с информацией о заявке пользователя
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты от пользователя {user_state.name}:\n\nТип перевода: {user_state.type}\nСумма обмена: {user_state.amount} €\nIBAN: {user_state.iban}\nБанк: {user_state.bank}\nСвяжитесь с пользователем по идентификатору @{message.from_user.username} для уточнения деталей обмена.")
        # Отправляем сообщение пользователю со стартовым сообщением и клавиатурой с кнопками курс, инструкция и обмен
        bot.send_message(message.chat.id, "Я могу снова помочь тебе купить или продать евро по выгодному курсу. 💶", reply_markup=create_keyboard())
        save_user_id(message.chat.id)
    elif text == "Отмена":
        # Если текст равен "Отмена", отправляем сообщение пользователю с информацией о том, что его заявка отменена и предложением начать заново
        bot.send_message(message.chat.id, "Твоя заявка на обмен валюты отменена. 😢\nЕсли ты хочешь начать заново, нажми кнопку Обмен на главной клавиатуре или напиши мне /start, чтобы узнать, что я умею.", reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, "Ты можешь оформить заявку по новой. 💶", reply_markup=create_keyboard())
    else:
        # Если текст не равен "Подтвердить", отправляем сообщение пользователю с просьбой нажать кнопку Подтвердить
        bot.send_message(message.chat.id, "Пожалуйста, нажми кнопку Подтвердить, если ты уверен в своей заявке.")
        # Переводим пользователя в режим ожидания ответа на подтверждение заявки
        bot.register_next_step_handler(message, process_confirm_step)

#------------------------------------------ОТЗЫВЫ-------------------------------#
        
def save_reviews():
    with open(reviews_file, mode="w") as file:
        # Записываем в файл весь словарь user_reviews в формате JSON
        json.dump(user_reviews, file)
        
def load_reviews():
    try:
        with open(reviews_file, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Если файл не существует, вернуть пустой словарь
    except json.JSONDecodeError:
        return {}  # Если JSON некорректен, вернуть пустой словарь
    
@bot.message_handler(commands=["reviews"])
def reviews(message):
    # Если пользователь отправил хотя бы одну заявку, отправляем ему сообщение с двумя кнопками "Написать отзыв" и "Просмотреть отзывы"
    bot.send_message(message.chat.id, "Ты можешь написать отзыв о моей работе или просмотреть отзывы других пользователей. Выбери одну из опций на клавиатуре.", reply_markup=create_review_keyboard())
    # Переводим пользователя в режим ожидания ответа на выбор опции
    bot.register_next_step_handler(message, process_review_step)

def process_review_step(message):
    text = message.text
    if text == "Написать отзыв":
        if  check_user_id(message.chat.id) == False:
            bot.send_message(message.chat.id, "К сожалению, ты не можешь написать отзыв, так как ты ещё не оформил ни одной заявки. 😭", reply_markup=types.ReplyKeyboardRemove())
            start(message)
        elif check_user_id_review(message.chat.id) == True:
            bot.send_message(message.chat.id, "Вы уже оставили отзыв. Вы не можете оставить отзыв снова.", reply_markup=types.ReplyKeyboardRemove())
            start(message)
        else:
            bot.send_message(message.chat.id, "Напиши свой отзыв о моей работе. Я буду рада услышать твое мнение. 😊", reply_markup=create_cancel())
            bot.register_next_step_handler(message, process_write_step)
    elif text == "Просмотреть отзывы":
        view_reviews(message)
    elif text == "Отмена":
        # Если текст равен "Отмена", отправляем сообщение пользователю с информацией о том, что его заявка отменена и предложением начать заново
        bot.send_message(message.chat.id, "Отменено", reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, "Переход в главное меню", reply_markup=create_keyboard())
    elif is_admin(message.from_user.id) and text == "Очистка":
        process_clear_step(message)
    else:
        # Если текст не соответствует одному из вариантов, отправляем сообщение пользователю с просьбой выбрать одну из опций на клавиатуре
        bot.send_message(message.chat.id, "Пожалуйста, выбери одну из опций на клавиатуре: Написать отзыв или Просмотреть отзывы.")
        # Переводим пользователя в режим ожидания ответа на выбор опции
        bot.register_next_step_handler(message, process_review_step)

def process_write_step(message):
    text = message.text
    user_id = message.chat.id
    if user_id not in user_reviews:
        user_reviews[user_id] = []
    user_reviews[user_id] = [f"✅ @{message.from_user.username}: {text}\n"] #{user_state.name}
    save_reviews()
    bot.send_message(message.chat.id, "Спасибо за твой отзыв! 🙏\nЯ очень ценю твое мнение. 😊\n", reply_markup=create_keyboard())
    bot.send_message(ADMIN_ID, f"Пользователь @{message.from_user.username} оставил свой отзыв: {text}")
    save_user_id_review(message.chat.id)

def view_reviews(message):
    user_reviews = load_reviews()
    if user_reviews:
        reviews_text = ""
        for user_id, reviews in user_reviews.items():
            for review in reviews:
                reviews_text += f"{review}\n"
        bot.send_message(message.chat.id, f"Вот что пишут о моей работе другие пользователи:\n\n{reviews_text}", reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, f"▼Переход в главное меню▼", reply_markup=create_keyboard())
    else:
        bot.send_message(message.chat.id, "Пока еще нет ни одного отзыва о моей работе. 😢\nЕсли ты хочешь написать свой отзыв, нажми кнопку Написать отзыв на клавиатуре или напиши мне /reviews.", reply_markup=create_keyboard())

def clear_all():
    # Очищаем словарь user_reviews с помощью метода clear
    user_reviews.clear()
    # Открываем файл reviews.json на запись с помощью функции open и параметра mode="w"
    with open(reviews_file, mode="w") as file:
        file.write("")
    with open(userID_file, mode="w") as file:
        file.write("")
    with open(userID_file_review, mode="w") as file:
        file.write("")

def process_clear_step(message): #АДМИНОВСКАЯ ОЧИСТКА СПИСКОВ
    # Получаем текст сообщения пользователя
    text = message.text
    # Проверяем, что текст равен "Очистить"
    if text == "Очистка":
        clear_all()
        # Отправляем сообщение пользователю с информацией о том, что список отзывов очищен
        bot.send_message(message.chat.id, "Списки очищены. 😊\nВо всех файлах были обнулины отзывы и списки людей с их ID, кто оформлял заявки!!!", reply_markup=types.ReplyKeyboardRemove())

#----------------------СОХРАНЕНИЯ-МЕТРИКИ------------------------------#
def save_user_id(user_id):
    try:
        # Открываем файл для записи
        with open(userID_file, 'w') as file:
            # Создаем словарь с user_id
            data = {'user_id': user_id}
            # Записываем данные в файл в формате JSON
            json.dump(data, file)
        print(f'User ID {user_id} успешно сохранен в файл {userID_file}')
    except Exception as e:
        print(f'Ошибка при сохранении User ID: {e}')

def save_user_id_review(user_id):
    try:
        # Открываем файл для записи
        with open(userID_file_review, 'w') as file:
            # Создаем словарь с user_id
            data = {'user_id': user_id}
            # Записываем данные в файл в формате JSON
            json.dump(data, file)
        print(f'User ID {user_id} успешно сохранен в файл {userID_file_review}')
    except Exception as e:
        print(f'Ошибка при сохранении User ID: {e}')

# Функция для проверки наличия user_id в файле JSON
def check_user_id(user_id):
    try:
        # Открываем файл для чтения
        with open(userID_file, 'r') as file:
            # Загружаем данные из файла
            data = json.load(file)
            # Проверяем наличие user_id в данных
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

# Функция для проверки наличия user_id в файле JSON
def check_user_id_review(user_id):
    try:
        # Открываем файл для чтения
        with open(userID_file_review, 'r') as file:
            # Загружаем данные из файла
            data = json.load(file)
            # Проверяем наличие user_id в данных
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
#------------------------ЗАПУСК------------------#
bot.polling() 