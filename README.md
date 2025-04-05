# Telegram Currency Exchange Bot (v0.2.3)

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
- **Admin Management**: 
  - Special commands and notifications for administrators
  - Support for multiple admin accounts
- **Enhanced Anti-spam Protection**: 30-second cooldown between exchange requests
- **User-friendly Interface**: Uses inline keyboards for navigation throughout the bot
- **Message Cleanup**: Advanced message history cleaning functionality
- **Request Cancellation**: Users can cancel exchange requests after submission
- **Improved Data Collection**: Additional user information for better service

## What's New in v2.3
- Completely redesigned message cleanup system for better chat hygiene
- Added name input field in the exchange process
- Improved user experience with more intuitive interface
- Enhanced validation for exchange amounts and user inputs
- Added proxy support for improved connectivity in regions with restrictions
- Fixed bugs in the review system
- Added support for a secondary admin account
- Message priority system for better admin notifications
- Fixed multiple issues related to the review section
- Changed minimum exchange amounts to 10,000 RUB for buying and 100 EUR for selling

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

3. Configure the bot token and admin IDs in the script (see Configuration section)

4. Run the bot:
```bash
python main.py
```

## Configuration

The bot requires the following configuration:

- **Bot Token**: Obtained from BotFather on Telegram
- **Admin IDs**: Telegram user IDs of administrators who will receive notifications
- **Proxy Settings** (optional): HTTP proxy configuration for improved connectivity in regions with restrictions

For production use, it's recommended to store these values as environment variables instead of hardcoding them in the script.

## Usage

### User Commands

- `/start` - Start the bot and show the main menu

### Exchange Process

1. User selects "Обмен" (Exchange) from the main menu
2. User chooses transaction type (Buy or Sell)
3. User selects their bank from available options
4. User enters the amount (minimum 10,000 RUB for buying or 100 EUR for selling)
5. User provides their IBAN
6. User enters their name and surname in Latin characters
7. User confirms or cancels the exchange request
8. User can cancel the request even after submission
9. Admin receives notification about the new request
10. Admin contacts the user to complete the exchange

### Review System

1. User selects "Отзывы" (Reviews) from the main menu
2. User can choose to write a review (if they've completed an exchange)
3. User can choose to read reviews from other customers
4. Reviews are stored with the username of the reviewer

## Data Storage

The bot uses JSON files to store:
- User IDs who have completed exchanges (`users_id.json`)
- User IDs who have left reviews (`users_id_review.json`)
- Review content (`reviews.json`)

## License

This project is available for private use. All rights reserved. 

## Developers

(C) 2023 Aleksander Samarin, Blagoveshchensk, Russia 
