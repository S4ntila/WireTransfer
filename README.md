# WireTransfer 1.4.6

<p align="center">
  <img src="icon.jpg" alt="WireTransfer Logo" width="200" height="200">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.4.6-blue.svg" alt="Version 1.4.6">
  <img src="https://img.shields.io/badge/python-3.6+-green.svg" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/license-Private-red.svg" alt="License: Private">
</p>

<p align="center">
  <a href="#rus">Русский</a> |
  <a href="#eng">English</a>
</p>

---

<a id="rus"></a>
# 🇷🇺 WireTransfer: Телеграм-бот для обмена валюты

## 📋 Обзор
WireTransfer — это удобный Telegram бот для обработки операций обмена между евро и рублями. Бот разработан для безопасной и эффективной обработки валютных операций с интуитивно понятным интерфейсом.

## ✨ Основные возможности
- 💱 **Обмен валюты**: Простой интерфейс для покупки или продажи евро
- 📊 **Актуальные курсы**: Автоматическое получение курсов валют от ЦБ РФ
- 🔄 **Подтверждение операций**: Двухэтапная система подтверждения для безопасности
- 📝 **Система отзывов**: Возможность оставить и просмотреть отзывы с модерацией
- 🔄 **Резервное копирование**: Сохранение данных пользователей и их восстановление

## 🚀 Подробная инструкция по установке

### Установка из исходного кода

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/yourusername/wiretransfer.git
   cd wiretransfer
   ```

2. **Установка зависимостей**
   ```bash
   pip install pyTelegramBotAPI requests
   ```
   или с помощью файла requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройка конфигурации**
   - Откройте файл `main.py` в текстовом редакторе
   - Замените `YOUR_BOT_TOKEN_HERE` на токен бота, полученный от [@BotFather](https://t.me/BotFather)
   - Установите ID администраторов (`ADMIN_ID` и `ADMIN_ID2`) — это Telegram ID пользователей, которые будут иметь права администратора

4. **Создание директории для бэкапов**
   ```bash
   mkdir backup
   ```

5. **Инициализация файлов данных**
   Создайте пустые JSON файлы:
   ```bash
   echo "{}" > users_id.json
   echo "{}" > users_id_review.json
   echo "{}" > reviews.json
   echo "{}" > reviews_confirm.json
   ```

6. **Запуск бота**
   ```bash
   python main.py
   ```

## 🛠️ Решение проблем

### Распространенные проблемы:

1. **Бот не запускается**
   - Проверьте токен бота в настройках
   - Убедитесь, что все зависимости установлены
   - Проверьте доступ к сети и прокси-настройки

2. **Ошибка "Cannot connect to host api.telegram.org"**
   - Проверьте подключение к интернету
   - Если вы используете прокси, раскомментируйте и настройте прокси-секцию в коде

3. **Проблемы с файлами данных**
   - Убедитесь, что все необходимые JSON файлы созданы
   - Проверьте права доступа к файлам
   - Восстановите файлы из резервных копий (если есть)

## 💻 Руководство пользователя

### Для клиентов:
1. **Начало работы**: Отправьте команду `/start` боту
2. **Обмен валюты**: Нажмите кнопку "Обмен" и следуйте инструкциям
3. **Просмотр курса**: Используйте кнопку "Курс" для отображения текущего курса обмена
4. **Инструкции**: Нажмите "Инструкция" для получения подробной информации о процессе обмена
5. **Отзывы**: Оставьте свой отзыв или просмотрите отзывы других пользователей

### Для администраторов:
1. **Панель администратора**: Доступна после авторизации с ADMIN_ID
2. **Управление данными**: Возможность очистки файлов и просмотра данных пользователей
3. **Модерация отзывов**: Одобрение или отклонение отзывов пользователей
4. **Резервное копирование**: Создание и восстановление резервных копий данных

## 🔄 Обновления в версии 1.4.6
- 🔧 **Исправлена обработка ID пользователей**: Исправлена проблема с обработкой ID пользователей при отклонении отзывов администратором
- 🛡️ **Улучшенная стабильность системы**: Увеличена надежность работы с пользовательскими данными
- 📝 **Оптимизированная работа с отзывами**: Улучшена работа системы модерации отзывов
- 🔄 **Техническое обслуживание**: Обновлен код для обеспечения лучшей производительности

---

<a id="eng"></a>
# 🇬🇧 WireTransfer: Telegram Currency Exchange Bot

## 📋 Overview
WireTransfer is a convenient Telegram bot for processing exchange operations between euros and rubles. The bot is designed for safe and efficient currency transactions with an intuitive interface.

## ✨ Key Features
- 💱 **Currency Exchange**: Simple interface for buying or selling euros
- 📊 **Current Rates**: Automatic retrieval of exchange rates from the Central Bank of Russia
- 🔄 **Operation Confirmation**: Two-stage confirmation system for security
- 📝 **Review System**: Ability to leave and view reviews with moderation
- 🔄 **Backup System**: User data saving and recovery

## 🚀 Detailed Installation Guide

### Installation from Source Code

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/wiretransfer.git
   cd wiretransfer
   ```

2. **Install Dependencies**
   ```bash
   pip install pyTelegramBotAPI requests
   ```
   or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Settings**
   - Open `main.py` in a text editor
   - Replace `YOUR_BOT_TOKEN_HERE` with the bot token obtained from [@BotFather](https://t.me/BotFather)
   - Set administrator IDs (`ADMIN_ID` and `ADMIN_ID2`) - these are Telegram IDs of users who will have admin rights

4. **Create Backup Directory**
   ```bash
   mkdir backup
   ```

5. **Initialize Data Files**
   Create empty JSON files:
   ```bash
   echo "{}" > users_id.json
   echo "{}" > users_id_review.json
   echo "{}" > reviews.json
   echo "{}" > reviews_confirm.json
   ```

6. **Launch the Bot**
   ```bash
   python main.py
   ```

## 🛠️ Troubleshooting

### Common Issues:

1. **Bot Won't Start**
   - Check the bot token in settings
   - Make sure all dependencies are installed
   - Verify network access and proxy settings

2. **Error "Cannot connect to host api.telegram.org"**
   - Check your internet connection
   - If you're using a proxy, uncomment and configure the proxy section in the code

3. **Data File Problems**
   - Ensure all necessary JSON files are created
   - Check file access permissions
   - Restore files from backups (if available)

## 💻 User Guide

### For Clients:
1. **Getting Started**: Send the `/start` command to the bot
2. **Currency Exchange**: Click the "Exchange" button and follow the instructions
3. **View Rate**: Use the "Rate" button to display the current exchange rate
4. **Instructions**: Click "Instructions" for detailed information about the exchange process
5. **Reviews**: Leave your review or view reviews from other users

### For Administrators:
1. **Admin Panel**: Available after authentication with ADMIN_ID
2. **Data Management**: Ability to clear files and view user data
3. **Review Moderation**: Approve or reject user reviews
4. **Backup**: Create and restore data backups

## 🔄 Updates in Version 1.4.6
- 🔧 **Fixed User ID Processing**: Fixed issue with user ID handling when administrators reject reviews
- 🛡️ **Enhanced System Stability**: Increased reliability of user data management
- 📝 **Optimized Review Processing**: Improved review moderation system
- 🔄 **Technical Maintenance**: Updated code to ensure better performance

---

<p align="center">
  <strong>© 2023 Aleksander Samarin. All rights reserved.</strong><br>
  Telegram: @RSantila | Email: ssaannttiillaa@gmail.com
</p>