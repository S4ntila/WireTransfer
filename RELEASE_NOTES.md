# WireTransfer: История изменений / Release Notes

<p align="center">
  <img src="icon.jpg" alt="WireTransfer Logo" width="150" height="150">
</p>

## Версия 1.2.7 / Version 1.2.7 (27.09.2023)

### 🇷🇺 Что нового
- **Исправлена система подтверждения отзывов**: Администраторы теперь могут корректно одобрять или отклонять отзывы пользователей
- **Функция удаления отзывов из буфера**: Добавлена возможность удаления отзывов из буфера подтверждения
- **Оптимизация для мобильных устройств**: Улучшен процесс удаления сообщений для более плавной работы на мобильных устройствах
- **Исправлен баг проверки отзывов**: Устранена проблема с проверкой предыдущих отправок отзывов пользователем

### 🇬🇧 What's New
- **Fixed Review Confirmation System**: Administrators can now correctly approve or reject user reviews
- **Review Buffer Deletion Function**: Added ability to delete reviews from confirmation buffer
- **Mobile Device Optimization**: Improved message deletion process for smoother operation on mobile devices
- **Fixed Review Checking Bug**: Resolved issue with checking user's previous review submissions

### 📋 Технические детали / Technical Details
- Переработана функция `check_user_id_review()` для корректной проверки наличия предыдущих отзывов
- Добавлена функция `delete_review_from_buffer()` для удаления отзывов из буфера
- Оптимизирована функция `delete_the_fucking_message()` для более эффективной работы
- Улучшено форматирование данных в файлах JSON

## Версия 1.1.0 / Version 1.1.0 (предыдущая / previous)

### 🇷🇺 Что было добавлено
- Система модерации отзывов с опциями одобрения и отклонения
- Обновленная панель администратора
- Просмотр данных пользователей для администраторов
- Улучшенное управление сообщениями

### 🇬🇧 What Was Added
- Review moderation system with approval and rejection options
- Updated admin panel
- User data viewing for administrators
- Improved message management

## Установка обновления / Update Installation

### 🇷🇺 Инструкция по обновлению
1. Скачайте новую версию .exe файла из [последнего релиза](https://github.com/yourusername/wiretransfer/releases)
2. Или обновите исходный код и перезапустите бот:
   ```bash
   git pull
   python main.py
   ```

### 🇬🇧 Update Instructions
1. Download the new .exe file from the [latest release](https://github.com/yourusername/wiretransfer/releases)
2. Or update the source code and restart the bot:
   ```bash
   git pull
   python main.py
   ```

## Известные проблемы / Known Issues

### 🇷🇺 Текущие ограничения
- В некоторых случаях при проверке предыдущих отзывов пользователя может требоваться дополнительная верификация

### 🇬🇧 Current Limitations
- In some cases, checking previous user reviews may require additional verification

---

<p align="center">
  <strong>© 2023 Aleksander Samarin. All rights reserved.</strong><br>
  Telegram: @RSantila | Email: ssaannttiillaa@gmail.com
</p> 