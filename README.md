# WireTransfer

<p align="center">
  <img src="icon.jpg" alt="WireTransfer Logo" width="200" height="200">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.3.5-blue.svg" alt="Version 1.3.5">
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
Профессиональный Telegram-бот для обработки обменных операций между евро и рублями. WireTransfer обеспечивает безопасный и удобный интерфейс для пользователей, включает инструменты администрирования, отображение актуальных курсов валют и усовершенствованную систему отзывов.

### 🚀 Основные функции
- **Обмен валюты**: Покупка/продажа евро с минимальными суммами от 10 000 RUB или 100 EUR
- **Актуальные курсы**: Динамическое получение курсов от ЦБ РФ с наценкой
- **Улучшенная система отзывов**: Отзывы пользователей с модерацией администратором (одобрение/отклонение)
- **Банки**: Поддержка операций через Сбербанк, Тинькофф, Райффайзен
- **Оптимизация для мобильных устройств**: Улучшенное удаление сообщений для мобильных пользователей
- **Резервное копирование**: Автоматическое создание резервных копий данных и возможность восстановления

### ⚙️ Установка
1. Скачайте готовый exe-файл из [последнего релиза](https://github.com/yourusername/wiretransfer/releases) или
2. Установите вручную:
   - Клонировать репозиторий
   - Установить зависимости: `pip install pyTelegramBotAPI requests`
   - Настроить токен бота и ID администраторов в `main.py`
   - Запустить бот: `python main.py`

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
- Создание и восстановление резервных копий данных

### 🆕 Что нового в версии 1.3.5
- Добавлена функция резервного копирования и восстановления файлов данных
- Сохранены все функции версии 1.3.1
- Улучшен интерфейс администратора с новыми кнопками
- Обновлена документация об известных проблемах

Подробности смотрите в [RELEASE_NOTES.md](RELEASE_NOTES.md)

### 🔒 Безопасность
- Валидация входных данных
- Очистка истории сообщений
- Проверка имени латиницей
- Хранение минимума необходимых данных
- Резервное копирование данных

---

<a id="eng"></a>
## 🇬🇧 EUR/RUB Currency Exchange Telegram Bot

### 📝 Description
A professional Telegram bot for processing exchange operations between euros and rubles. WireTransfer provides a secure and user-friendly interface, comprehensive admin tools, real-time currency rates, and an improved review system.

### 🚀 Key Features
- **Currency Exchange**: Buy/sell euros with minimum amounts of 10,000 RUB or 100 EUR
- **Real-time Rates**: Dynamic rate fetching from the Central Bank of Russia with markup
- **Enhanced Review System**: User reviews with admin moderation (approve/reject)
- **Banks**: Support for operations via Sberbank, Tinkoff, Raiffeisen
- **Mobile Optimization**: Improved message deletion for mobile users
- **Backup System**: Automatic data backup and recovery options

### ⚙️ Installation
1. Download the ready-to-use exe file from [latest release](https://github.com/yourusername/wiretransfer/releases) or
2. Manual installation:
   - Clone the repository
   - Install dependencies: `pip install pyTelegramBotAPI requests`
   - Configure bot token and admin IDs in `main.py`
   - Run the bot: `python main.py`

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
- Create and restore data backups

### 🆕 What's New in Version 1.3.5
- Added backup and restore functionality for data files
- Maintained all functionality from version 1.3.1
- Enhanced admin interface with new buttons
- Updated documentation about known issues

See [RELEASE_NOTES.md](RELEASE_NOTES.md) for details

### 🔒 Security
- Input validation
- Message history cleanup
- Latin name verification
- Minimal necessary data storage
- Data backup and recovery

---

<p align="center">
  <strong>© 2023 Aleksander Samarin. All rights reserved.</strong><br>
  Telegram: @RSantila | Email: ssaannttiillaa@gmail.com
</p>