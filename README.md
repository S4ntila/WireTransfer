# 💱 WireTransfer

<p align="center">
  <img src="icon.png" alt="WireTransfer Logo" width="220" height="220" style="box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.5.2-brightgreen.svg?style=for-the-badge" alt="Version 1.5.2">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg?style=for-the-badge&logo=python" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/license-Private-red.svg?style=for-the-badge" alt="License: Private">
  <img src="https://img.shields.io/badge/telegram-Bot-informational.svg?style=for-the-badge&logo=telegram" alt="Telegram Bot">
</p>

<p align="center">
  <a href="#rus"><b>🇷🇺 Русский</b></a> |
  <a href="#eng"><b>🇬🇧 English</b></a>
</p>

---

<a id="rus"></a>
# 🇷🇺 WireTransfer: Телеграм-бот для обмена валюты

## 📋 Обзор
**WireTransfer** — это многофункциональный Telegram бот, созданный для безопасного и эффективного обмена валюты между евро и рублями. Бот предоставляет интуитивно понятный интерфейс с актуальными курсами валют, позволяя пользователям быстро и удобно создавать заявки на обмен.

## ✨ Ключевые особенности
- 💱 **Интеллектуальный обмен валюты**: Простой и понятный процесс создания заявки на покупку или продажу евро
- 📊 **Актуальные рыночные курсы**: Автоматическое получение и расчет курсов из нескольких источников (Alfabit + Binance)
- 🔒 **Двухэтапное подтверждение**: Повышенная безопасность при проведении операций
- 🌟 **Система отзывов с модерацией**: Позволяет пользователям делиться опытом и читать отзывы других пользователей
- 💾 **Резервное копирование данных**: Мгновенное создание и восстановление резервных копий всех пользовательских данных
- 🛠️ **Гибкое управление курсами**: Администраторы могут настраивать множители для курсов покупки и продажи
- 👤 **Расширенные функции для администраторов**: Просмотр данных пользователей, управление отзывами и настройка системы

## 🚀 Подробное руководство по установке

### 📥 Установка из исходного кода

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/S4ntila/WireTransfer.git
   cd wiretransfer
   ```

2. **Установка зависимостей**
   ```bash
   pip install -r requirements.txt
   ```
   
   *Или установите необходимые библиотеки вручную:*
   ```bash
   pip install pyTelegramBotAPI requests
   ```

3. **Настройка конфигурации**
   - Откройте файл `main.py` в текстовом редакторе
   - Укажите токен бота, полученный от [@BotFather](https://t.me/BotFather)
   - Установите ID администраторов в переменных `ADMIN_ID` и `ADMIN_ID2`

4. **Создание необходимых директорий**
   ```bash
   mkdir backup
   ```

5. **Инициализация файлов данных**
   ```bash
   echo "{}" > users_id.json
   echo "{}" > users_id_review.json
   echo "{}" > reviews.json
   echo "{}" > reviews_confirm.json
   echo '{"buy": 1.055, "sell": 1}' > multipliers.json
   ```

6. **Запуск бота**
   ```bash
   python main.py
   ```

## 🛠️ Устранение неполадок

### 🔍 Часто возникающие проблемы:

1. **Бот не запускается**
   - Проверьте правильность токена бота в настройках
   - Убедитесь, что все зависимости установлены
   - Проверьте доступ к интернету и настройки прокси (при необходимости)

2. **Ошибка соединения с API Telegram**
   - Убедитесь в стабильности вашего подключения к интернету
   - Если используете прокси, проверьте его настройки и доступность
   - Проверьте, не заблокирован ли доступ к api.telegram.org

3. **Проблемы с получением курса валют**
   - Проверьте доступность сервисов alfabit.org и binance.com
   - Проверьте структуру ответа API на случай изменений в формате данных
   - При необходимости обновите алгоритм получения курса в функции `get_eur_rub()`

4. **Проблемы с файлами данных**
   - Убедитесь, что все необходимые JSON файлы созданы и доступны для чтения/записи
   - Проверьте права доступа к файлам и директориям
   - Воспользуйтесь функцией восстановления из резервной копии

## 💻 Руководство пользователя

### 👥 Для клиентов:

1. **Начало работы**
   - Откройте бота в Telegram и отправьте команду `/start`
   - Используйте интерактивное меню для навигации

2. **Обмен валюты**
   - Нажмите кнопку "Обмен" в главном меню
   - Выберите тип операции (покупка или продажа евро)
   - Укажите банк, сумму, IBAN и ваше имя
   - Подтвердите заявку и ожидайте связи с администратором

3. **Просмотр курса валют**
   - Используйте кнопку "Курс" для отображения актуальных курсов
   - Курсы обновляются в реальном времени из нескольких источников

4. **Ознакомление с инструкциями**
   - Нажмите "Инструкция" для получения подробной информации о процессе обмена
   - Следуйте указанным шагам для успешного завершения транзакции

5. **Работа с отзывами**
   - Используйте раздел "Отзывы" для просмотра мнений других пользователей
   - Оставьте свой отзыв после завершения обмена (доступно только после успешного обмена)

### 👨‍💼 Для администраторов:

1. **Расширенная панель управления**
   - Автоматически доступна при авторизации с ADMIN_ID
   - Включает дополнительные функции для управления ботом

2. **Управление курсами валют**
   - Используйте функцию "Изменить курс" для корректировки множителей
   - Настраивайте курсы покупки и продажи отдельно для гибкости системы

3. **Работа с данными**
   - Просматривайте информацию о пользователях через "Данные пользователей"
   - При необходимости выполняйте очистку файлов через соответствующую функцию

4. **Модерация отзывов**
   - Получайте уведомления о новых отзывах
   - Одобряйте или отклоняйте отзывы пользователей для публикации

5. **Управление резервными копиями**
   - Создавайте резервные копии всех данных одним нажатием
   - При необходимости восстанавливайте данные из резервных копий

## 🔄 Обновления в версии 1.5.2

### 🌟 Новые возможности
- **Усовершенствованный алгоритм получения курса**: Теперь данные берутся с платформы Alfabit.org для более точного курса USD/RUB
- **Обновлен токен бота**: Новая версия использует обновленный токен для повышенной безопасности
- **Оптимизирована работа с администраторами**: Улучшена система уведомлений и управления
- **Обновлены алгоритмы расчета**: Незначительные улучшения в вычислении курсов

### 🔧 Технические улучшения
- **Улучшенный код**: Более эффективный алгоритм получения и обработки данных
- **Обновление безопасности**: Устранены потенциальные уязвимости в системе
- **Оптимизация производительности**: Сокращено время ответа и улучшена стабильность бота
- **Актуализация API**: Работа с новыми версиями API внешних сервисов

---

<a id="eng"></a>
# 🇬🇧 WireTransfer: Telegram Currency Exchange Bot

## 📋 Overview
**WireTransfer** is a multifunctional Telegram bot designed for safe and efficient currency exchange between euros and rubles. The bot provides an intuitive interface with up-to-date exchange rates, allowing users to quickly and conveniently create exchange requests.

## ✨ Key Features
- 💱 **Smart Currency Exchange**: Simple and straightforward process for creating buy or sell euro requests
- 📊 **Real-time Market Rates**: Automatic retrieval and calculation of rates from multiple sources (Alfabit + Binance)
- 🔒 **Two-stage Confirmation**: Enhanced security when conducting operations
- 🌟 **Moderated Review System**: Allows users to share experiences and read reviews from others
- 💾 **Data Backup**: Instant creation and restoration of backups for all user data
- 🛠️ **Flexible Rate Management**: Administrators can adjust multipliers for buy and sell rates
- 👤 **Advanced Admin Functions**: View user data, manage reviews, and configure the system

## 🚀 Detailed Installation Guide

### 📥 Installation from Source Code

1. **Clone the Repository**
   ```bash
   git clone https://github.com/S4ntila/WireTransfer.git
   cd wiretransfer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   *Or install necessary libraries manually:*
   ```bash
   pip install pyTelegramBotAPI requests
   ```

3. **Configure Settings**
   - Open `main.py` in a text editor
   - Set the bot token obtained from [@BotFather](https://t.me/BotFather)
   - Set administrator IDs in the `ADMIN_ID` and `ADMIN_ID2` variables

4. **Create Required Directories**
   ```bash
   mkdir backup
   ```

5. **Initialize Data Files**
   ```bash
   echo "{}" > users_id.json
   echo "{}" > users_id_review.json
   echo "{}" > reviews.json
   echo "{}" > reviews_confirm.json
   echo '{"buy": 1.055, "sell": 1}' > multipliers.json
   ```

6. **Launch the Bot**
   ```bash
   python main.py
   ```

## 🛠️ Troubleshooting

### 🔍 Common Issues:

1. **Bot Won't Start**
   - Check the bot token in settings
   - Make sure all dependencies are installed
   - Check internet access and proxy settings (if necessary)

2. **Error Connecting to Telegram API**
   - Ensure your internet connection is stable
   - If using a proxy, check its settings and availability
   - Check if access to api.telegram.org is blocked

3. **Problems with Exchange Rate Retrieval**
   - Check the availability of alfabit.org and binance.com services
   - Verify the API response structure in case of format changes
   - Update the rate retrieval algorithm in the `get_eur_rub()` function if necessary

4. **Data File Problems**
   - Ensure all necessary JSON files are created and accessible for reading/writing
   - Check file and directory access permissions
   - Use the restore function from backup

## 💻 User Guide

### 👥 For Clients:

1. **Getting Started**
   - Open the bot in Telegram and send the `/start` command
   - Use the interactive menu for navigation

2. **Currency Exchange**
   - Click the "Exchange" button in the main menu
   - Choose the operation type (buying or selling euros)
   - Specify the bank, amount, IBAN, and your name
   - Confirm the request and wait for administrator contact

3. **Viewing Exchange Rates**
   - Use the "Rate" button to display current rates
   - Rates are updated in real-time from multiple sources

4. **Reviewing Instructions**
   - Click "Instructions" for detailed information about the exchange process
   - Follow the steps indicated for successful transaction completion

5. **Working with Reviews**
   - Use the "Reviews" section to view opinions from other users
   - Leave your own review after completing an exchange (available only after successful exchange)

### 👨‍💼 For Administrators:

1. **Extended Control Panel**
   - Automatically available when authenticated with ADMIN_ID
   - Includes additional functions for bot management

2. **Exchange Rate Management**
   - Use the "Change Rate" function to adjust multipliers
   - Configure buy and sell rates separately for system flexibility

3. **Data Management**
   - View user information through "User Data"
   - Clean files when necessary using the appropriate function

4. **Review Moderation**
   - Receive notifications about new reviews
   - Approve or reject user reviews for publication

5. **Backup Management**
   - Create backups of all data with one click
   - Restore data from backups when necessary

## 🔄 Updates in Version 1.5.2

### 🌟 New Features
- **Enhanced Rate Retrieval Algorithm**: Data is now sourced from Alfabit.org platform for more accurate USD/RUB rates
- **Updated Bot Token**: New version uses an updated token for increased security
- **Optimized Administrator Functionality**: Improved notification and management system
- **Updated Calculation Algorithms**: Minor improvements in rate calculations

### 🔧 Technical Improvements
- **Improved Code**: More efficient data retrieval and processing algorithm
- **Security Updates**: Eliminated potential vulnerabilities in the system
- **Performance Optimization**: Reduced response time and improved bot stability
- **API Actualization**: Working with new versions of external service APIs

---

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red.svg?style=for-the-badge" alt="Made with love">
</p>

<p align="center">
  <strong>© 2024 Aleksander Samarin. All rights reserved.</strong><br>
  Telegram: <a href="https://t.me/RSantila">@RSantila</a> | Email: ssaannttiillaa@gmail.com
</p>