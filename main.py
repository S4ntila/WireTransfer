# Импортируем нужные библиотеки
import requests
import telebot
from telebot import types
import os # Модуль для работы с переменными окружения

# Получаем токен для нашего бота от BotFather
ADMIN_ID = "ID_USER"

# Создаем экземпляр бота с помощью библиотеки pyTelegramBotAPI
bot = telebot.TeleBot('BOT_TOKEN')

# Определяем функцию для получения курса евро к рублю с помощью API Центробанка России
def get_eur_rub():
    # Запрашиваем данные по ссылке
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    # Проверяем, что ответ успешный
    if response.status_code == 200:
        # Преобразуем данные в формат JSON
        data = response.json()
        # Извлекаем курс евро к рублю из словаря
        eur_rub = data["Valute"]["EUR"]["Value"]
        # Возвращаем курс в виде числа с плавающей точкой
        return float(eur_rub)
    else:
        # Если ответ не успешный, возвращаем None
        return None

# Определяем функцию для добавления 6 процентов к числу
def add_six_percent(number):
    # Умножаем число на 1.06 и округляем до двух знаков после запятой
    return round(number * 1.06, 2)

# Определяем функцию для форматирования числа с разделителем тысяч и знаком рубля
def format_rub(number):
    # Преобразуем число в строку с разделителем тысяч
    number_str = "{:,}".format(number)
    # Заменяем запятые на пробелы
    number_str = number_str.replace(",", " ")
    # Добавляем знак рубля в конце строки
    number_str += " ₽"
    # Возвращаем отформатированную строку
    return number_str

# Определяем функцию для создания клавиатуры с кнопками курс, инструкция и обмен
def create_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса InlineKeyboardMarkup
    keyboard = types.InlineKeyboardMarkup()
    # Создаем три кнопки с помощью класса InlineKeyboardButton и текстом "Курс", "Инструкция" и "Обмен"
    button_rate = types.InlineKeyboardButton("Курс", callback_data="rate")
    button_instruction = types.InlineKeyboardButton("Инструкция", callback_data="instruction")
    button_exchange = types.InlineKeyboardButton("Обмен", callback_data="exchange") # Это новая кнопка, которую я добавил
    # Добавляем кнопки на клавиатуру в один ряд с помощью метода add
    keyboard.add(button_rate, button_instruction, button_exchange) # Здесь я добавил новую кнопку в конец ряда
    # Возвращаем клавиатуру
    return keyboard

# Определяем функцию для создания клавиатуры с кнопками купить, продать и назад
def create_exchange_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса InlineKeyboardMarkup
    keyboard = types.InlineKeyboardMarkup()
    # Создаем три кнопки с помощью класса InlineKeyboardButton и текстом "Купить", "Продать" и "Назад"
    button_buy = types.InlineKeyboardButton("Купить", callback_data="buy")
    button_sell = types.InlineKeyboardButton("Продать", callback_data="sell")
    button_back = types.InlineKeyboardButton("Назад", callback_data="back")
    # Добавляем кнопки на клавиатуру в два ряда с помощью метода add
    keyboard.add(button_buy, button_sell)
    keyboard.add(button_back)
    # Возвращаем клавиатуру
    return keyboard

# Определяем функцию для создания клавиатуры с кнопкой отмены
def create_cancel_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса InlineKeyboardMarkup
    keyboard = types.InlineKeyboardMarkup()
    # Создаем одну кнопку с помощью класса InlineKeyboardButton и текстом "Отмена"
    button_cancel = types.InlineKeyboardButton("Отмена", callback_data="cancel")
    # Добавляем кнопку на клавиатуру с помощью метода add
    keyboard.add(button_cancel)
    # Возвращаем клавиатуру
    return keyboard

# Определяем функцию для создания клавиатуры с кнопкой подтверждения
def create_confirm_keyboard():
    # Создаем экземпляр клавиатуры с помощью класса InlineKeyboardMarkup
    keyboard = types.InlineKeyboardMarkup()
    # Создаем одну кнопку с помощью класса InlineKeyboardButton и текстом "Подтвердить"
    button_confirm = types.InlineKeyboardButton("Подтвердить", callback_data="confirm")
    # Добавляем кнопку на клавиатуру с помощью метода add
    keyboard.add(button_confirm)
    # Возвращаем клавиатуру
    return keyboard

# Импортируем модуль time для работы со временем
import time

# Создаем глобальную переменную для хранения времени последнего уведомления
last_notification_time = None

# Определяем функцию для отправки уведомления администратору бота о новой заявке на обмен валюты
def send_notification(chat_id, type, amount, name, iban):
    # Получаем текущее время в секундах с помощью функции time.time
    current_time = time.time()
    # Проверяем, что переменная last_notification_time не None и что прошло не менее 15 минут с момента последнего уведомления
    if last_notification_time is not None and current_time - last_notification_time < 15 * 60:
        # Если это так, то пропускаем отправку уведомления и выводим сообщение в консоль
        print("Пропускаем отправку уведомления, так как прошло менее 15 минут с момента последнего уведомления.")
        return
    # Иначе, продолжаем отправку уведомления
    # Составляем текст сообщения с данными о заявке и эмодзи
    text = f"Новая заявка на обмен валюты! 🚨\n\nТип: {type}\nСумма: {amount} €\nФамилия и имя: {name}\nIBAN: {iban}\n\nЧтобы связаться с клиентом, напиши ему в этом чате: {chat_id}"
    # Отправляем сообщение администратору бота с помощью метода send_message и параметром chat_id, который равен ID администратора бота (вставь свой ID сюда)
    bot.send_message(ADMIN_ID, text)
    # Обновляем значение переменной last_notification_time на текущее время
    last_notification_time = current_time
    
# Определяем обработчик команды /start, которая выводит приветственное сообщение и клавиатуру с кнопками курс, инструкция и обмен
@bot.message_handler(commands=["start"])
def start(message):
    # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру
    bot.send_message(message.chat.id, "Привет, это Сидней. Я твой AI-ассистент по обмену валюты. 😊\nЯ могу помочь тебе купить или продать евро по выгодному курсу. 💶\nЧтобы начать, выбери одну из опций на клавиатуре или напиши мне /help, чтобы узнать, что я умею.", reply_markup=create_keyboard())
    
# Определяем обработчик команды /rate, которая выводит курс евро к рублю и добавляет к нему по 6 процентов
@bot.message_handler(commands=["rate"])
def rate(message):
    # Получаем курс евро к рублю с помощью функции get_eur_rub
    eur_rub = get_eur_rub()
    # Проверяем, что курс не None
    if eur_rub is not None:
        # Добавляем по 6 процентов к курсу покупки и продажи евро с помощью функции add_six_percent
        eur_rub_buy = add_six_percent(eur_rub)
        eur_rub_sell = add_six_percent(eur_rub * 0.99) # предполагаем, что курс продажи на 1 процент ниже курса покупки
        # Форматируем курсы с помощью функции format_rub
        eur_rub_buy_str = format_rub(eur_rub_buy)
        eur_rub_sell_str = format_rub(eur_rub_sell)
        # Составляем текст сообщения с курсами и эмодзи
        text = f"Курс евро к рублю на сегодня:\n\n🔵 Покупка: {eur_rub_buy_str}\n🔴 Продажа: {eur_rub_sell_str}"
        # Отправляем сообщение пользователю с помощью метода send_message
        bot.send_message(message.chat.id, text)
    else:
        # Если курс None, значит произошла ошибка при запросе данных
        # Отправляем сообщение пользователю с извинением и эмодзи
        bot.send_message(message.chat.id, "Извини, я не смог получить данные по курсу евро. 😢\nПопробуй позже или напиши мне /start, чтобы узнать, что я умею.")

# Определяем обработчик команды /instruction, которая выводит инструкцию по обмену валюты через бота
@bot.message_handler(commands=["instruction"])
def instruction(message):
    # Составляем текст сообщения с инструкцией и эмодзи
    text = "Если ты хочешь обменять валюту через меня, вот что тебе нужно сделать:\n\n1. Подаёшь заявку на обмен валюты через вкладку «Обмен» в главном меню бота. Потребуется предоставить информацию о типе перевода, сумме, реквизиты твоей карты для зачисления перевода. 📝\n2. В ближайшее время я свяжусь с тобой для уточнения курса и готовности выполнить перевод. А также предоставлю реквизиты для оплаты. 💳\n3. Далее следует отправить средства в течении 15 минут(!) после получения реквизитов, а также предоставить чек. При надобности, может потребоваться указать комментарий при переводе, о чем предупрежу заранее. 💸\n4. Получаешь средства на указанные тобой в заявке реквизиты (~30-60 минут, после отправки тобой средств). 💰\n5. Предоставляешь мне скрин прихода средств. 📸"
    # Отправляем сообщение пользователю с помощью метода send_message
    bot.send_message(message.chat.id, text)

# Определяем обработчик команды /exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
@bot.message_handler(commands=["exchange"])
def exchange(message):
    # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру
    bot.send_message(message.chat.id, "Добро пожаловать в меню обмена валюты. 🙌\nЗдесь ты можешь купить или продать евро по выгодному курсу. 💶\nВыбери одну из опций на клавиатуре или нажми \"Назад\", чтобы вернуться в главное меню.", reply_markup=create_exchange_keyboard())

# Определяем обработчик колбэков от кнопок на клавиатурах
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
        # Если данные равны "exchange", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(call.message)
    elif data == "buy":
        # Если данные равны "buy", отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
        bot.send_message(call.message.chat.id, "Ты хочешь купить евро по курсу {eur_rub_buy_str}. 💶\nВведите сумму в евро, которую ты хочешь купить, или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.".format(eur_rub_buy_str=format_rub(add_six_percent(get_eur_rub()))), reply_markup=create_cancel_keyboard())
        # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции buy_amount, которая запрашивает сумму в евро
        bot.register_next_step_handler(call.message, buy_amount)
    elif data == "sell":
        # Если данные равны "sell", отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
        bot.send_message(call.message.chat.id, "Ты хочешь продать евро по курсу {eur_rub_sell_str}. 💶\nВведите сумму в евро, которую ты хочешь продать, или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.".format(eur_rub_sell_str=format_rub(add_six_percent(get_eur_rub() * 0.99))), reply_markup=create_cancel_keyboard())
        # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции sell_amount, которая запрашивает сумму в евро
        bot.register_next_step_handler(call.message, sell_amount)
    elif data == "back":
        # Если данные равны "back", вызываем функцию start, которая выводит приветственное сообщение и клавиатуру с кнопками курс, инструкция и обмен
        start(call.message)
    elif data == "cancel":
        # Если данные равны "cancel", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(call.message)
    elif data == "confirm":
        # Если данные равны "confirm", вызываем функцию buy_confirm или sell_confirm в зависимости от типа заявки на обмен валюты, которую хранит глобальная переменная exchange_type
        if exchange_type == "buy":
            buy_confirm(call.message, exchange_amount, exchange_name, exchange_iban) # Добавь call в качестве параметра
        elif exchange_type == "sell":
            sell_confirm(call.message, exchange_amount, exchange_name, exchange_iban) # Добавь call в качестве параметра
    # Убери этот блок кода:
    # Добавляем обработчик колбэков для кнопки подтверждения
    # elif data == "confirm": # Это новая строка, которую я добавила
    #     # Если данные равны "confirm", отправляем сообщение пользователю с помощью метода answer_callback_query и параметром show
        bot.answer_callback_query(call.id, "Твоя заявка на обмен валюты подтверждена. ✅\nПожалуйста, подожди, пока я свяжусь с тобой для уточнения деталей.", show_alert=True) # Это новая строка, которую я добавила

# Определяем глобальные переменные для хранения данных о заявке на обмен валюты
exchange_type = None # Тип заявки: купить или продать
exchange_amount = None # Сумма в евро
# Фамилия и имя
exchange_name = None
# IBAN
exchange_iban = None

# Определяем функцию для запрашивания суммы в евро при покупке
def buy_amount(message):
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст не равен "Отмена"
    if text != "Отмена":
        # Пытаемся преобразовать текст в число с плавающей точкой
        try:
            # Присваиваем переменной amount значение числа
            amount = float(text)
            # Проверяем, что число положительное и не больше 10000
            if amount > 0 and amount <= 10000:
                # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
                bot.send_message(message.chat.id, "Ты хочешь купить {amount} € за {rub} ₽. 💶💰\nВведите свою фамилию и имя или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.".format(amount=amount, rub=format_rub(amount * add_six_percent(get_eur_rub()))), reply_markup=create_cancel_keyboard())
                # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции buy_name, которая запрашивает фамилию и имя
                bot.register_next_step_handler(message, buy_name, amount)
            else:
                # Если число отрицательное или больше 10000, отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
                bot.send_message(message.chat.id, "Извини, но ты можешь купить только от 0.01 до 10000 евро за раз. 😅\nПожалуйста, введи корректную сумму или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.", reply_markup=create_cancel_keyboard())
                # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции buy_amount, которая запрашивает сумму в евро
                bot.register_next_step_handler(message, buy_amount)
        except ValueError:
            # Если текст не является числом, отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
            bot.send_message(message.chat.id, "Извини, но я не понимаю, что ты написал. 😕\nПожалуйста, введи сумму в евро или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.", reply_markup=create_cancel_keyboard())
            # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции buy_amount, которая запрашивает сумму в евро
            bot.register_next_step_handler(message, buy_amount)
    else:
        # Если текст равен "Отмена", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для запрашивания фамилии и имени при покупке
def buy_name(message, amount):
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст не равен "Отмена"
    if text != "Отмена":
        # Присваиваем переменной name значение текста
        name = text
        # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
        bot.send_message(message.chat.id, "Твоя фамилия и имя: {name}. 👤\nВведите свой IBAN или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.".format(name=name), reply_markup=create_cancel_keyboard())
        # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции buy_iban, которая запрашивает IBAN
        bot.register_next_step_handler(message, buy_iban, amount, name)
    else:
        # Если текст равен "Отмена", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для запрашивания IBAN при покупке
def buy_iban(message, amount, name):
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст не равен "Отмена"
    if text != "Отмена":
        # Присваиваем переменной iban значение текста
        iban = text
        # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой подтверждения
        bot.send_message(message.chat.id, "Твой IBAN: {iban}. 🏦\nТы хочешь купить {amount} € за {rub} ₽. 💶💰\nТвоя фамилия и имя: {name}. 👤\nЕсли все верно, нажми \"Подтвердить\", чтобы оформить заявку на обмен валюты. ✅\nЕсли хочешь изменить данные, нажми \"Отмена\" и начни заново.".format(iban=iban, amount=amount, rub=format_rub(amount * add_six_percent(get_eur_rub())), name=name), reply_markup=create_confirm_keyboard())
        # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции buy_confirm, которая подтверждает заявку на обмен валюты
        bot.register_next_step_handler(message, buy_confirm, amount, name, iban)
    else:
        # Если текст равен "Отмена", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для подтверждения заявки на обмен валюты при покупке
def buy_confirm(message, amount, name, iban):
    bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты!\n\nТип: Покупка\nСумма: {amount} €\nФамилия и имя: {name}\nIBAN: {iban}\n\nЧтобы связаться с клиентом, напиши ему в этом чате: {message.chat_id}")
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст равен "Подтвердить"
    if text == "Подтвердить":
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты!\n\nТип: Покупка\nСумма: {amount} €\nФамилия и имя: {name}\nIBAN: {iban}\n\nЧтобы связаться с клиентом, напиши ему в этом чате: {message.chat_id}")
        # Отправляем уведомление пользователю с помощью метода answer_callback_query и параметром show_alert
        bot.answer_callback_query(message.id, "Твоя заявка на обмен валюты подтверждена. ✅\nПожалуйста, подожди, пока я свяжусь с тобой для уточнения деталей.", show_alert=True) # Замени message.id на call.id
        # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопками курс, инструкция и обмен
        #bot.send_message(message.chat.id, "Твоя заявка на обмен валюты успешно оформлена. 🎉\nВ ближайшее время я свяжусь с тобой для уточнения курса и готовности выполнить перевод. 💳\nСпасибо, что пользуешься моими услугами. 🙏", reply_markup=create_keyboard())
        # Отправляем уведомление администратору бота о новой заявке на обмен валюты с помощью функции send_notification
        #send_notification(message.chat.id, "Купить", amount, name, iban)
    else:
# Если текст не равен "Подтвердить", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для запрашивания суммы в евро при продаже
def sell_amount(message):
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст не равен "Отмена"
    if text != "Отмена":
        # Пытаемся преобразовать текст в число с плавающей точкой
        try:
            # Присваиваем переменной amount значение числа
            amount = float(text)
            # Проверяем, что число положительное и не больше 10000
            if amount > 0 and amount <= 10000:
                # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
                bot.send_message(message.chat.id, "Ты хочешь продать {amount} € за {rub} ₽. 💶💰\nВведите свою фамилию и имя или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.".format(amount=amount, rub=format_rub(amount * add_six_percent(get_eur_rub() * 0.99))), reply_markup=create_cancel_keyboard())
                # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции sell_name, которая запрашивает фамилию и имя
                bot.register_next_step_handler(message, sell_name, amount)
            else:
                # Если число отрицательное или больше 10000, отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
                bot.send_message(message.chat.id, "Извини, но ты можешь продать только от 0.01 до 10000 евро за раз. 😅\nПожалуйста, введи корректную сумму или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.", reply_markup=create_cancel_keyboard())
                # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции sell_amount, которая запрашивает сумму в евро
                bot.register_next_step_handler(message, sell_amount)
        except ValueError:
            # Если текст не является числом, отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
            bot.send_message(message.chat.id, "Извини, но я не понимаю, что ты написал. 😕\nПожалуйста, введи сумму в евро или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.", reply_markup=create_cancel_keyboard())
            # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции sell_amount, которая запрашивает сумму в евро
            bot.register_next_step_handler(message, sell_amount)
    else:
        # Если текст равен "Отмена", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для запрашивания фамилии и имени при продаже
def sell_name(message, amount):
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст не равен "Отмена"
    if text != "Отмена":
        # Присваиваем переменной name значение текста
        name = text
        # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой отмены
        bot.send_message(message.chat.id, "Твоя фамилия и имя: {name}. 👤\nВведите свой IBAN или нажми \"Отмена\", чтобы вернуться в меню обмена валюты.".format(name=name), reply_markup=create_cancel_keyboard())
        # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции sell_iban, которая запрашивает IBAN
        bot.register_next_step_handler(message, sell_iban, amount, name)
    else:
        # Если текст равен "Отмена", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для запрашивания IBAN при продаже
def sell_iban(message, amount, name):
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст не равен "Отмена"
    if text != "Отмена":
        # Присваиваем переменной iban значение текста
        iban = text
        # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопкой подтверждения
        bot.send_message(message.chat.id, "Твой IBAN: {iban}. 🏦\nТы хочешь продать {amount} € за {rub} ₽. 💶💰\nТвоя фамилия и имя: {name}. 👤\nЕсли все верно, нажми \"Подтвердить\", чтобы оформить заявку на обмен валюты. ✅\nЕсли хочешь изменить данные, нажми \"Отмена\" и начни заново.".format(iban=iban, amount=amount, rub=format_rub(amount * add_six_percent(get_eur_rub() * 0.99)), name=name), reply_markup=create_confirm_keyboard())
        # Устанавливаем следующий шаг для обработки сообщения от пользователя с помощью метода register_next_step_handler и функции sell_confirm, которая подтверждает заявку на обмен валюты
        bot.register_next_step_handler(message, sell_confirm, amount, name, iban)
    else:
        # Если текст равен "Отмена", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Определяем функцию для подтверждения заявки на обмен валюты при продаже
def sell_confirm(message, amount, name, iban): # Добавь call в качестве параметра
    # Получаем текст сообщения от пользователя
    text = message.text
    # Проверяем, что текст равен "Подтвердить"
    if text == "Подтвердить":
        bot.send_message(ADMIN_ID, f"Новая заявка на обмен валюты! 🚨\n\nТип: Продажа\nСумма: {amount} €\nФамилия и имя: {name}\nIBAN: {iban}\n\nЧтобы связаться с клиентом, напиши ему в этом чате: {message.chat_id}")
        # Отправляем уведомление пользователю с помощью метода answer_callback_query и параметром show_alert
        bot.answer_callback_query(message.id, "Твоя заявка на обмен валюты подтверждена. ✅\nПожалуйста, подожди, пока я свяжусь с тобой для уточнения деталей.", show_alert=True) # Замени message.id на call.id
        # Отправляем сообщение пользователю с помощью метода send_message и параметром reply_markup, чтобы показать клавиатуру с кнопками курс, инструкция и обмен
        bot.send_message(message.chat.id, "Твоя заявка на обмен валюты успешно оформлена. 🎉\nВ ближайшее время я свяжусь с тобой для уточнения курса и готовности выполнить перевод. 💳\nСпасибо, что пользуешься моими услугами. 🙏", reply_markup=create_keyboard())
        # Отправляем уведомление администратору бота о новой заявке на обмен валюты с помощью функции send_notification
        send_notification(message.chat.id, "Продать", amount, name, iban)
    else:
# Если текст не равен "Подтвердить", вызываем функцию exchange, которая выводит меню обмена валюты и клавиатуру с кнопками купить, продать и назад
        exchange(message)

# Запускаем бота с помощью метода polling
bot.polling()
