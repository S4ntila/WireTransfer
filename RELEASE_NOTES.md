# 💱 WireTransfer 1.5.2 (09.01.2024)

<p align="center">
  <img src="icon.png" alt="WireTransfer Logo" width="180" height="180" style="border-radius: 15px;">
</p>

## 🇷🇺 Обновления в версии 1.5.2

### 🌟 Новые возможности:
- Переход на платформу **Alfabit.org** для получения курса доллара к рублю
- Обновлен алгоритм вычисления курса евро-рубль через промежуточные курсы
- Актуализирован токен бота для повышенной безопасности
- Оптимизирована система уведомлений для администраторов
- Улучшены множители курсов для более точных расчетов

### 📚 Технические изменения:
- Функция `get_eur_rub()` теперь получает USD/RUB с Alfabit.org и EUR/USD с Binance
- Обновлена система уведомлений администраторов в функции `confirm_exit()`
- Улучшена обработка ошибок при получении курсов валют
- Обновлен токен бота и идентификаторы администраторов
- Оптимизирован код для более стабильной работы с API внешних сервисов

## 🇬🇧 Updates in Version 1.5.2

### 🌟 New Features:
- Switched to **Alfabit.org** platform for USD to RUB exchange rate
- Updated EUR-RUB calculation algorithm using intermediate rates
- Updated bot token for increased security
- Optimized notification system for administrators
- Improved rate multipliers for more accurate calculations

### 📚 Technical Changes:
- The `get_eur_rub()` function now fetches USD/RUB from Alfabit.org and EUR/USD from Binance
- Updated administrator notification system in the `confirm_exit()` function
- Improved error handling when retrieving exchange rates
- Updated bot token and administrator IDs
- Optimized code for more stable interaction with external service APIs

# WireTransfer: История изменений / Release Notes

<p align="center">
  <img src="icon.png" alt="WireTransfer Logo" width="150" height="150">
</p>

## Версия 1.5.0 / Version 1.5.0 (29.07.2023)

### 🇷🇺 Что нового
- **Новый источник курса валют**: Переход с API Центробанка России на платформу Binance для более точных рыночных курсов
- **Усовершенствованный алгоритм расчета**: Курс EUR/RUB теперь рассчитывается через промежуточный курс USD
- **Обновлены множители курса**: Изменены базовые значения множителей для покупки (1.055) и продажи (1.0)
- **Оптимизированный код**: Повышена эффективность работы с API и обработки данных

### 🇬🇧 What's New
- **New Exchange Rate Source**: Switched from Russian Central Bank API to Binance platform for more accurate market rates
- **Enhanced Calculation Algorithm**: EUR/RUB rate is now calculated through USD intermediate rate
- **Updated Rate Multipliers**: Changed base values for buy (1.055) and sell (1.0) multipliers
- **Optimized Code**: Improved efficiency of API handling and data processing

### 📋 Технические детали / Technical Details
- Переработана функция `get_eur_rub()` для использования данных с Binance вместо ЦБ РФ
- Курс теперь вычисляется на основе двух отдельных курсов: USD/RUB и EUR/USD
- Изменены значения по умолчанию в функции `load_multipliers()` на более актуальные
- Сохранены все улучшения из предыдущих версий, включая систему резервного копирования и обработку отзывов

## Версия 1.4.6 / Version 1.4.6 (10.07.2023)

### 🇷🇺 Что нового
- **Исправлена обработка ID пользователей**: Улучшен алгоритм обработки ID пользователей при отклонении отзывов администратором
- **Улучшенная стабильность системы**: Увеличена надежность работы с пользовательскими данными и файлами
- **Оптимизированная работа с отзывами**: Улучшена система модерации и обработки отзывов
- **Техническое обслуживание**: Обновлен код для обеспечения лучшей производительности и стабильности

### 🇬🇧 What's New
- **Fixed User ID Processing**: Improved algorithm for handling user IDs when administrators reject reviews
- **Enhanced System Stability**: Increased reliability of user data and file management
- **Optimized Review Processing**: Improved review moderation and processing system
- **Technical Maintenance**: Updated code to ensure better performance and stability

### 📋 Технические детали / Technical Details
- Обновлен механизм обработки ID пользователей при отклонении отзывов для более корректной работы
- Улучшены функции, связанные с обработкой файлов данных
- Улучшена структура кода для более надежной работы с пользовательскими данными
- Сохранены все функциональные улучшения из предыдущих версий

## Версия 1.4.5 / Version 1.4.5 (03.10.2023)

### 🇷🇺 Что нового
- **Улучшенная обработка отзывов**: Исправлена проблема с обработкой ID пользователей при отклонении отзывов администратором
- **Обновленные инструкции**: Модифицированы инструкции для более четкого объяснения процесса обмена валюты
- **Улучшенная загрузка множителей**: Добавлены значения по умолчанию при отсутствии файла множителей или при ошибке чтения
- **Дополнительные настройки курса**: Добавлена возможность отдельного управления курсом для определенных пользователей

### 🇬🇧 What's New
- **Improved Review Processing**: Fixed issue with user ID handling when administrators reject reviews
- **Updated Instructions**: Modified instructions for clearer explanation of the exchange process
- **Enhanced Multiplier Loading**: Added default values when multiplier file is missing or when reading errors occur
- **Additional Rate Settings**: Added ability to manage separate exchange rates for specific users

### 📋 Технические детали / Technical Details
- Обновлена функция `load_multipliers()` для возвращения значений по умолчанию при отсутствии файла
- Изменен текст инструкций в функции `instructions()` для улучшения пользовательского опыта
- Добавлены улучшения для более стабильной работы с отзывами пользователей
- Сохранены все улучшения функциональности из предыдущих версий

## Версия 1.4.2 / Version 1.4.2 (30.09.2023)

### 🇷🇺 Что нового
- **Управление курсом обмена**: Добавлена возможность для администраторов изменять множители курса покупки и продажи
- **Улучшенный процесс обмена**: Пользователь всегда вводит сумму в евро, бот автоматически рассчитывает эквивалент в рублях
- **Умное хранение множителей**: Система сохраняет множители курса в отдельном файле для быстрой настройки и восстановления
- **Расширенные уведомления**: Администраторы получают более детальную информацию с конвертацией сумм

### 🇬🇧 What's New
- **Exchange Rate Management**: Added ability for administrators to change multipliers for buying and selling rates
- **Improved Exchange Process**: Users always enter amounts in euros, bot automatically calculates the ruble equivalent
- **Smart Multiplier Storage**: System stores rate multipliers in a separate file for quick configuration and recovery
- **Enhanced Notifications**: Administrators receive more detailed information with amount conversion

### 📋 Технические детали / Technical Details
- Добавлен файл `multipliers.json` для хранения множителей курса покупки и продажи
- Обновлена функция `get_eur_rub_rate()` для использования множителей из файла
- Добавлены функции для изменения множителей курса: `change_rate()`, `change_buy()`, `change_sell()`, `confirm_buy()`, `confirm_sell()`, `apply_buy()`, `apply_sell()`
- В меню администратора добавлена кнопка "Изменить курс" для быстрого доступа к управлению курсом
- Переработан процесс заполнения заявки: пользователь всегда вводит сумму в евро
- Улучшен вывод информации для пользователя и администратора, теперь показывается конвертация в обоих направлениях

## Версия 1.3.8 / Version 1.3.8 (05.10.2023)

### 🇷🇺 Что нового
- **Улучшенное форматирование чисел**: Целые числа теперь отображаются без десятичной части для лучшей читаемости
- **Улучшенное отображение курсов валют**: Курсы округляются до 1 знака после запятой вместо 2
- **Модифицированные алгоритмы расчета**: Обновлены коэффициенты для расчета курсов покупки и продажи
- **Улучшен пользовательский опыт**: Более понятное представление числовых значений

### 🇬🇧 What's New
- **Improved Number Formatting**: Whole numbers now displayed without decimal part for better readability
- **Enhanced Currency Rate Display**: Rates are rounded to 1 decimal place instead of 2
- **Modified Calculation Algorithms**: Updated coefficients for buy and sell rate calculations
- **Improved User Experience**: Clearer presentation of numerical values

### 📋 Технические детали / Technical Details
- Добавлена функция `round_if_zero()` для правильного отображения целых чисел
- Изменены коэффициенты для расчета курса: покупка - 1.057 (было 1.053), продажа - осталась 0.99
- Округление значений курса теперь производится до 1 знака после запятой вместо 2
- Сохранены все улучшения и функциональность из предыдущих версий

## Версия 1.3.6 / Version 1.3.6 (30.09.2023)

### 🇷🇺 Что нового
- **Улучшена документация**: Полностью переработан README файл для улучшения понимания процесса установки и запуска
- **Расширены инструкции по установке**: Добавлены пошаговые инструкции для различных способов установки
- **Оптимизирована система резервного копирования**: Улучшена надежность сохранения и восстановления данных
- **Улучшен пользовательский интерфейс**: Добавлены подробные инструкции и пояснения для пользователей

### 🇬🇧 What's New
- **Improved Documentation**: Completely redesigned README file to enhance understanding of installation and launch processes
- **Expanded Installation Instructions**: Added step-by-step instructions for various installation methods
- **Optimized Backup System**: Improved reliability of data saving and recovery
- **Enhanced User Interface**: Added detailed instructions and explanations for users

### 📋 Технические детали / Technical Details
- Переработан файл README.md с более подробными инструкциями по установке и настройке
- Добавлен раздел по устранению неполадок для решения распространенных проблем
- Улучшена структура документации для более легкого понимания
- Сохранены и улучшены все функциональные возможности из предыдущих версий

## Версия 1.3.5 / Version 1.3.5 (28.09.2023)

### 🇷🇺 Что нового
- **Добавлена система резервного копирования**: Реализованы функции создания резервных копий и восстановления файлов данных
- **Расширена панель администратора**: Добавлены кнопки для работы с резервными копиями
- **Оптимизирован код**: Улучшена структура существующих функций
- **Сохранены исправления из 1.3.1**: Все улучшения текста и интерфейса из предыдущей версии

### 🇬🇧 What's New
- **Added Backup System**: Implemented functions for creating backups and restoring data files
- **Extended Admin Panel**: Added buttons for working with backups
- **Optimized Code**: Improved the structure of existing functions
- **Preserved Fixes from 1.3.1**: All text and interface improvements from the previous version

### 📋 Технические детали / Technical Details
- Добавлена функция `backup_files()` для создания резервных копий всех важных файлов данных
- Добавлена функция `restore_files()` для восстановления данных из резервных копий
- Добавлен импорт библиотеки `shutil` для работы с файлами
- Расширены возможности администратора с новыми кнопками "Рез. Копирование" и "Восстановление"
- Обновлена версия в документации и комментариях

## Версия 1.3.1 / Version 1.3.1 (28.09.2023)

### 🇷🇺 Что нового
- **Улучшения текста интерфейса**: Исправлены формулировки в разделе отзывов для большей ясности
- **Исправлены несоответствия в UI**: Унифицирован текст при просмотре отзывов
- **Выявлены дополнительные проблемы**: Обнаружена проблема с исчезновением сообщений после отправки отзыва

### 🇬🇧 What's New
- **UI Text Improvements**: Corrected phrasing in reviews section for better clarity
- **Fixed UI Inconsistencies**: Unified text when viewing reviews
- **Additional Issues Identified**: Discovered issue with message disappearance after review submission

### 📋 Технические детали / Technical Details
- Исправлен текст в функции `reviews()` (строка 169): изменено "другие пользователи" на "пользователи"
- Исправлен текст в функции `reviews_read()` (строка 252): унифицирован стиль отображения отзывов
- Сохранена вся функциональность версии 1.3.0
- Добавлено описание обнаруженной проблемы с исчезновением сообщений

## Версия 1.3.0 / Version 1.3.0 (27.09.2023)

### 🇷🇺 Что нового
- **Исправлена ошибка удаления отзывов**: Решена проблема с неполным удалением отзывов при отклонении администратором
- **Улучшена проверка существующих заявок**: Система теперь проверяет и предупреждает о дублирующихся заявках
- **Оптимизирован порядок операций**: Изменен порядок выполнения команд для более логичного потока работы
- **Улучшена работа с файловой системой**: Более эффективная очистка и обработка файлов данных

### 🇬🇧 What's New
- **Fixed Review Deletion Issue**: Resolved problem with incomplete review deletion when rejected by administrator
- **Improved Existing Request Checking**: System now checks and warns about duplicate requests
- **Optimized Operation Order**: Changed command execution order for more logical workflow
- **Enhanced File System Operation**: More efficient data file clearing and processing

### 📋 Технические детали / Technical Details
- Изменена функция `check_user_id_review()` для использования более надежного метода проверки
- Добавлена проверка существующих ID пользователей при сохранении в `save_user_id()` и `save_user_id_review()`
- Переработан порядок операций в функциях `iban_check()` и `name_check()` для лучшей обработки команды `/start`
- Улучшена очистка файлов в функции `delete_user_info_about()`
- Добавлено логирование результата проверки при отклонении отзыва

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
1. Обновите исходный код и перезапустите бот:
   ```bash
   git pull
   python main.py
   ```

### 🇬🇧 Update Instructions
1. Update the source code and restart the bot:
   ```bash
   git pull
   python main.py
   ```

## Известные проблемы / Known Issues

### 🇷🇺 Текущие ограничения
- В некоторых случаях при проверке предыдущих отзывов пользователя может требоваться дополнительная верификация
- При отклонении отзыва администратором ID пользователя не удаляется из системы
- Сообщения могут не исчезать после отправки отзыва пользователем

### 🇬🇧 Current Limitations
- In some cases, checking previous user reviews may require additional verification
- When an administrator rejects a review, the user ID is not removed from the system
- Messages may not disappear after a user submits a review

---

<p align="center">
  <strong>© 2023 Aleksander Samarin. All rights reserved.</strong><br>
  Telegram: @RSantila | Email: ssaannttiillaa@gmail.com
</p> 