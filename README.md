# WireTransfer

<p align="center">
  <img src="icon.jpg" alt="WireTransfer Logo" width="200" height="200">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.1.0-blue.svg" alt="Version 1.1.0">
  <img src="https://img.shields.io/badge/python-3.6+-green.svg" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/license-Private-red.svg" alt="License: Private">
</p>

<p align="center">
  <a href="#rus">Русский</a> |
  <a href="#eng">English</a>
</p>

---

<a id="rus"></a>
## 🇷🇺 Телеграм-бот для обмена валюты EUR/RUB

### 📝 Описание
Профессиональный Telegram-бот для обработки обменных операций между евро и рублями. WireTransfer обеспечивает безопасный и удобный интерфейс для пользователей, включает инструменты администрирования, отображение актуальных курсов валют и систему отзывов.

### 🚀 Основные функции
- **Обмен валюты**: Покупка/продажа евро с минимальными суммами от 10 000 RUB или 100 EUR
- **Актуальные курсы**: Динамическое получение курсов от ЦБ РФ с наценкой
- **Система отзывов**: Отзывы пользователей с модерацией администратором
- **Банки**: Поддержка операций через Сбербанк, Тинькофф, Райффайзен

### ⚙️ Установка
1. Клонировать репозиторий
2. Установить зависимости: `pip install pyTelegramBotAPI requests`
3. Настроить токен бота и ID администраторов в `main.py`
4. Запустить бот: `python main.py`

### 👤 Руководство пользователя
1. **Запрос обмена**: 
   - Выберите "Обмен" → Тип операции → Банк → Введите сумму → IBAN → Имя/фамилия
   - Подтвердите детали и ожидайте связи с администратором

2. **Проверка курса**:
   - Нажмите "Курс" для просмотра актуальных ставок обмена

3. **Отзывы**:
   - Оставьте отзыв после совершения обмена
   - Просмотрите отзывы других пользователей

### 👨‍💼 Панель администратора
- Модерация отзывов (одобрение/отклонение)
- Просмотр заявок на обмен
- Просмотр данных пользователей
- Очистка системных файлов

### 🔒 Безопасность
- Валидация входных данных
- Очистка истории сообщений
- Проверка имени латиницей
- Хранение минимума необходимых данных

---

<a id="eng"></a>
## 🇬🇧 EUR/RUB Currency Exchange Telegram Bot

### 📝 Description
A professional Telegram bot for processing exchange operations between euros and rubles. WireTransfer provides a secure and user-friendly interface, comprehensive admin tools, real-time currency rates, and a review system.

### 🚀 Key Features
- **Currency Exchange**: Buy/sell euros with minimum amounts of 10,000 RUB or 100 EUR
- **Real-time Rates**: Dynamic rate fetching from the Central Bank of Russia with markup
- **Review System**: User reviews with admin moderation
- **Banks**: Support for operations via Sberbank, Tinkoff, Raiffeisen

### ⚙️ Installation
1. Clone the repository
2. Install dependencies: `pip install pyTelegramBotAPI requests`
3. Configure bot token and admin IDs in `main.py`
4. Run the bot: `python main.py`

### 👤 User Guide
1. **Exchange Request**: 
   - Select "Exchange" → Operation type → Bank → Enter amount → IBAN → Name/surname
   - Confirm details and wait for admin contact

2. **Check Rates**:
   - Click "Rate" to view current exchange rates

3. **Reviews**:
   - Leave a review after completing an exchange
   - View reviews from other users

### 👨‍💼 Admin Panel
- Review moderation (approve/reject)
- View exchange requests
- View user data
- Clear system files

### 🔒 Security
- Input validation
- Message history cleanup
- Latin name verification
- Minimal necessary data storage

---

<p align="center">
  <strong>© 2023 Aleksander Samarin. All rights reserved.</strong><br>
  Telegram: @RSantila | Email: ssaannttiillaa@gmail.com
</p>