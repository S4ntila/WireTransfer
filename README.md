# Telegram Currency Exchange Bot

A Telegram bot for EUR/RUB currency exchange that allows users to check current rates, get exchange instructions, and submit exchange requests. The bot features an admin notification system and user-friendly inline keyboards.

## Features

- **Real-time Currency Rates**: Fetches and displays current EUR/RUB exchange rates from the Central Bank of Russia
- **Exchange Instructions**: Provides detailed instructions on the exchange process
- **Exchange Functionality**: 
  - Buy euros with rubles
  - Sell euros for rubles
  - Maximum exchange amount: 10,000 EUR
- **Admin Notifications**: Notifies the admin about new exchange requests
- **User-friendly Interface**: Uses inline keyboards for easy navigation

## Requirements

- Python 3.6+
- telebot (pyTelegramBotAPI)
- requests

## Installation

1. Clone the repository or download the script

2. Install the required packages:
```bash
pip install pyTelegramBotAPI requests
```

3. Configure the bot token and admin ID (see Configuration section)

4. Run the bot:
```bash
python main.py
```

## Configuration

The bot requires the following configuration:

- **Bot Token**: Obtained from BotFather on Telegram
- **Admin ID**: Telegram user ID of the administrator who will receive notifications

These values are hardcoded in the script:
```python
ADMIN_ID = ID_USER
bot = telebot.TeleBot('BOT_TOKEN')
```

For production use, it's recommended to store these values as environment variables.

## Usage

### User Commands

- `/start` - Start the bot and show the main menu
- `/rate` - Check current EUR/RUB exchange rates
- `/instruction` - Get instructions on the exchange process
- `/exchange` - Access the exchange menu to buy or sell euros

### Exchange Process

1. User selects "Buy" or "Sell" from the exchange menu
2. User enters the amount in euros (0.01-10,000)
3. User provides their full name
4. User provides their IBAN
5. User confirms the exchange request
6. Admin receives a notification about the new request
7. Admin contacts the user to complete the exchange

## License

This project is available for private use. All rights reserved. 
