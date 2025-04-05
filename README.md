# Telegram Currency Exchange Bot (v0.1.3)

A Telegram bot for EUR/RUB currency exchange that allows users to check current rates, get exchange instructions, submit exchange requests, and write reviews. The bot features an admin notification system, anti-spam protection, and user-friendly interface with custom keyboards.

## Features

- **Real-time Currency Rates**: Fetches and displays current EUR/RUB exchange rates from the Central Bank of Russia
- **Exchange Instructions**: Provides detailed instructions on the exchange process
- **Exchange Functionality**: 
  - Buy euros with rubles
  - Sell euros for rubles
  - Bank selection (Sberbank, Tinkoff, Raiffeisen)
- **Review System**:
  - Users can write reviews after completing an exchange
  - Users can read reviews from other customers
- **Admin Management**: Special commands and notifications for administrators
- **Anti-spam Protection**: Prevents users from submitting too many requests
- **User-friendly Interface**: Uses both inline and reply keyboards for easy navigation

## Requirements

- Python 3.6+
- telebot (pyTelegramBotAPI)
- requests
- json (standard library)
- time (standard library)

## Installation

1. Clone the repository or download the script

2. Install the required packages:
```bash
pip install pyTelegramBotAPI requests
```

3. Configure the bot token and admin ID in the script (see Configuration section)

4. Run the bot:
```bash
python main.py
```

## Configuration

The bot requires the following configuration:

- **Bot Token**: Obtained from BotFather on Telegram
- **Admin ID**: Telegram user ID of the administrator who will receive notifications

For production use, it's recommended to store these values as environment variables instead of hardcoding them in the script.

## Usage

### User Commands

- `/start` - Start the bot and show the main menu
- `/rate` - Check current EUR/RUB exchange rates
- `/instruction` - Get instructions on the exchange process
- `/exchange` - Access the exchange menu to buy or sell euros
- `/reviews` - Access the reviews menu to write or read reviews

### Exchange Process

1. User selects "Обмен" (Exchange) from the main menu
2. User chooses transaction type (Buy or Sell)
3. User enters the amount in euros
4. User provides their full name
5. User provides their IBAN
6. User selects their bank from available options
7. User confirms the exchange request
8. Admin receives a notification about the new request
9. Admin contacts the user to complete the exchange

### Review System

1. User selects "Отзывы" (Reviews) from the main menu
2. User can choose to write a review (if they've completed an exchange)
3. User can choose to read reviews from other customers
4. Admin can clear all reviews if needed

## Data Storage

The bot uses JSON files to store:
- User IDs who have completed exchanges
- User IDs who have left reviews
- Review content

## License

This project is available for private use. All rights reserved. 