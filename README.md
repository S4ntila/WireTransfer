# Telegram Currency Exchange Bot (v0.1.9)

A Telegram bot for EUR/RUB currency exchange that allows users to check current rates, get exchange instructions, submit exchange requests, and write reviews. The bot features an admin notification system, anti-spam protection, and user-friendly interface with inline keyboards.

## Features

- **Real-time Currency Rates**: Fetches and displays current EUR/RUB exchange rates from the Central Bank of Russia
- **Exchange Instructions**: Provides detailed instructions on the exchange process
- **Exchange Functionality**: 
  - Buy euros with rubles
  - Sell euros for rubles 
  - Minimum amounts (100 EUR or 10,000 RUB)
  - Bank selection (Sberbank, Tinkoff, Raiffeisen)
- **Review System**:
  - Users can write reviews after completing an exchange
  - Users can read reviews from other customers
- **Admin Management**: Special commands and notifications for administrators
- **Enhanced Anti-spam Protection**: 30-second cooldown between exchange requests
- **User-friendly Interface**: Uses inline keyboards for navigation throughout the bot
- **Message Cleanup**: Automatically deletes user and bot messages to keep chat history clean
- **Request Cancellation**: Users can cancel exchange requests after submission

## What's New in v0.1.9
- Complete UI redesign using inline keyboards instead of reply keyboards
- Automatic message cleanup to keep chat history tidy
- Added ability to cancel exchange requests
- Improved validation for exchange amounts (minimum thresholds)
- Added proxy support for improved connectivity
- Enhanced error handling with temporary error messages
- Username-based identification instead of requiring full name
- Added message priority system for better admin notifications
- Fixed bugs in the review system

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
- **Proxy Settings** (optional): HTTP proxy configuration for improved connectivity

For production use, it's recommended to store these values as environment variables instead of hardcoding them in the script.

## Usage

### User Commands

- `/start` - Start the bot and show the main menu

### Exchange Process

1. User selects "Обмен" (Exchange) from the main menu
2. User chooses transaction type (Buy or Sell)
3. User selects their bank from available options
4. User enters the amount (minimum 100 EUR or 10,000 RUB)
5. User provides their IBAN
6. User confirms or cancels the exchange request
7. User can cancel the request even after submission
8. Admin receives notification about the new request
9. Admin contacts the user to complete the exchange

### Review System

1. User selects "Отзывы" (Reviews) from the main menu
2. User can choose to write a review (if they've completed an exchange)
3. User can choose to read reviews from other customers

## Data Storage

The bot uses JSON files to store:
- User IDs who have completed exchanges
- User IDs who have left reviews
- Review content

## License

This project is available for private use. All rights reserved. 