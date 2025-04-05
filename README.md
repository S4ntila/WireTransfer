# Telegram Currency Exchange Bot (v0.2.8)

A Telegram bot for EUR/RUB currency exchange that allows users to check current rates, get exchange instructions, submit exchange requests, and write reviews. The bot features an admin notification system, anti-spam protection, and user-friendly interface with inline keyboards.

## Features

- **Real-time Currency Rates**: Fetches and displays current EUR/RUB exchange rates from the Central Bank of Russia with dynamic loading indicators
- **Exchange Instructions**: Provides detailed instructions on the exchange process
- **Exchange Functionality**: 
  - Buy euros with rubles
  - Sell euros for rubles 
  - Minimum amounts (100 EUR or 10,000 RUB)
  - Bank selection (Sberbank, Tinkoff, Raiffeisen)
- **Review System**:
  - Users can write reviews after completing an exchange
  - Users can read reviews from other customers
  - Admin-only review moderation tools
- **Admin Management**: 
  - Special commands and notifications for administrators
  - Admin-specific interface with additional tools
  - Support for multiple admin accounts
  - Data file cleanup functionality
- **Enhanced User Experience**:
  - Name validation with regex to ensure correct format
  - Improved message handling with edit_message_text for dynamic updates
  - Better error handling for user inputs
  - Enhanced message history cleanup
- **User-friendly Interface**: Uses inline keyboards for navigation throughout the bot
- **Request Cancellation**: Users can return to the main menu at any point in the process
- **Security**: `/start` command recognition during data entry to allow user to restart

## What's New in v2.8
- Admin-specific interface with additional tools for managing the bot
- Admin-only review management with the ability to delete inappropriate reviews
- Improved message handling with edit_message_text for dynamic updates (especially visible in the rate display)
- Name validation with regex to ensure proper Latin characters
- More detailed admin notifications with username linking
- Added file cleanup functionality for administrators
- Enhanced error handling and user input validation
- Complete reorganization of function calls for better performance
- Improved welcome message and user interface
- Fixed bank selection issues with Raiffeisen Bank

## Requirements

- Python 3.6+
- telebot (pyTelegramBotAPI)
- requests
- json (standard library)
- time (standard library)
- re (regular expressions, standard library)
- os (standard library)

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
- **Admin IDs**: Telegram user IDs of administrators who will receive notifications and have access to admin tools
- **Proxy Settings** (optional): HTTP proxy configuration for improved connectivity in regions with restrictions

For production use, it's recommended to store these values as environment variables instead of hardcoding them in the script.

## Usage

### User Commands

- `/start` - Start the bot and show the main menu

### Admin Features

1. Special admin interface with additional tools
2. Review management with ability to delete reviews
3. Data file cleanup functionality
4. Detailed notifications about user activities

### Exchange Process

1. User selects "Обмен" (Exchange) from the main menu
2. User chooses transaction type (Buy or Sell)
3. User selects their bank from available options
4. User enters the amount (minimum 10,000 RUB for buying or 100 EUR for selling)
5. User provides their IBAN
6. User enters their name and surname in Latin characters (with validation)
7. User confirms or cancels the exchange request
8. Admin receives notification about the new request with user details
9. Admin contacts the user to complete the exchange

### Review System

1. User selects "Отзывы" (Reviews) from the main menu
2. User can choose to write a review (if they've completed an exchange)
3. User can choose to read reviews from other customers
4. Reviews are stored with the username of the reviewer
5. Admins can delete inappropriate reviews

## Data Storage

The bot uses JSON files to store:
- User IDs who have completed exchanges (`users_id.json`)
- User IDs who have left reviews (`users_id_review.json`)
- Review content (`reviews.json`)

## License

This project is available for private use. All rights reserved. 

## Developers

(C) 2023 Aleksander Samarin, Blagoveshchensk, Russia 