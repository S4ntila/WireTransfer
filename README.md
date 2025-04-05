# WireTransfer v0.3.7

<p align="center">
  <img src="https://img.shields.io/badge/version-0.3.7-blue.svg" alt="Version 0.3.7">
  <img src="https://img.shields.io/badge/python-3.6+-green.svg" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/license-Private-red.svg" alt="License: Private">
</p>

A professional Telegram bot for facilitating EUR/RUB currency exchanges with a secure and user-friendly interface. WireTransfer includes comprehensive admin tools, dynamic currency rates, enhanced review confirmation system, and improved user data storage.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Admin Guide](#admin-guide)
- [User Guide](#user-guide)
- [API Integration](#api-integration)
- [Security](#security)
- [Data Management](#data-management)
- [Troubleshooting](#troubleshooting)
- [Contact & Support](#contact--support)

## Overview

WireTransfer facilitates secure currency exchanges between EUR and RUB. Designed with both administrative controls and user-friendly interactions, it provides real-time exchange rates, processes requests, and handles customer reviews all within the Telegram interface.

### Target Users

- Individuals needing to exchange EUR/RUB currencies
- Businesses providing currency exchange services
- Administrators managing exchange operations

## Key Features

### Core Functionality

- **Currency Exchange Processing**
  - Euro purchase (RUB → EUR) with minimum 10,000 RUB
  - Euro sale (EUR → RUB) with minimum 100 EUR
  - Bank selection (Sberbank, Tinkoff, Raiffeisen)
  - IBAN and personal details collection
  - High transaction limits (up to 100,000,000 RUB and 1,000,000 EUR)

- **Real-time Exchange Rates**
  - Dynamic rate fetching from Central Bank of Russia
  - Custom rate formulation (buy rate: CBR rate × 1.053, sell rate: CBR rate × 0.99)
  - Loading indicator during rate retrieval
  - Formatted, readable rate presentation

- **Enhanced Review Management**
  - User-generated reviews with username identification
  - Admin approval system for review moderation
  - Review confirmation workflow with dedicated storage
  - Restricted to customers with completed transactions
  - Full reviews archive for credibility building

- **Transaction Instructions**
  - Detailed step-by-step process guide
  - Clear timeline expectations (15 min, 30-60 min periods)
  - Documentation requirements explanation

### Administrative Features

- **Admin Recognition System**
  - Multi-admin support with unique interfaces
  - Privileged access to sensitive functions
  - Admin-specific commands and notifications

- **Review Approval System**
  - Dedicated interface for review moderation
  - User-specific approval buttons for better tracking
  - Notification system for new review submissions
  - Separate storage for pending and approved reviews

- **Data Management Tools**
  - JSON database file cleanup functionality
  - Multi-user transaction tracking with array-based storage
  - Review moderation with deletion capability
  - Notification system for new requests and reviews

- **Security Enhancements**
  - Input validation with regex patterns
  - `/start` command recognition during all processes
  - Message history cleanup to prevent data exposure
  - Error handling with user-friendly messages

### User Experience

- **Interactive Navigation**
  - Intuitive inline keyboards
  - Contextual button presentation
  - Consistent back/cancel options
  - Multi-step form with validation

- **Dynamic Content Updates**
  - Real-time loading indicators
  - Message editing instead of new messages
  - Clean message history management
  - Responsive feedback system

## System Architecture

WireTransfer is structured around these key components:

1. **User State Management**
   - Class-based state tracking for multi-step processes
   - Transaction details storage during session
   - Reset functionality between operations

2. **API Integration**
   - Central Bank of Russia exchange rate integration
   - Custom rate calculations for buy/sell operations

3. **Callback System**
   - Button-based navigation framework
   - State-aware callbacks for process flow
   - Enhanced callbacks with parameter passing

4. **Data Persistence**
   - JSON-based storage for user transactions
   - Array-based user ID storage for multiple transaction support
   - Two-stage review system (pending and approved)
   - User identification tracking

5. **Admin Control Panel**
   - Privileged operations through role-based access
   - Data management tools
   - Review approval capabilities

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- Telegram account
- Bot token from BotFather

### Step-by-Step Setup

1. **Clone or download the repository**
   ```
   git clone https://your-repository-url.git
   cd wiretransfer-bot
   ```

2. **Install required packages**
   ```bash
   pip install pyTelegramBotAPI requests
   ```

3. **Configure the bot**
   - Edit `main.py` to set your bot token:
     ```python
     BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
     ```
   - Set admin IDs:
     ```python
     ADMIN_ID = 000000000  # Replace with actual Telegram ID
     ADMIN_ID2 = 000000000  # Replace with actual Telegram ID
     ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## Configuration

### Essential Settings

- `BOT_TOKEN`: Your Telegram bot token from BotFather
- `ADMIN_ID` and `ADMIN_ID2`: Telegram user IDs for administrators
- `admins`: Array of all admin IDs for privilege checks

### Optional Settings

- Proxy configuration for regions with Telegram restrictions
- Exchange rate multipliers (currently 1.053 for buying, 0.99 for selling)
- Minimum amounts (10,000 RUB, 100 EUR)
- Maximum amounts (100,000,000 RUB, 1,000,000 EUR)

### File Structure

- `main.py`: Core WireTransfer bot code
- `users_id.json`: Tracks multiple user transaction history with array storage
- `users_id_review.json`: Tracks users who submitted reviews
- `reviews.json`: Stores approved user reviews
- `reviews_confirm.json`: Stores pending reviews awaiting approval

## Admin Guide

### Admin Dashboard

As an admin, you'll receive an enhanced interface with additional options:

1. Access to the standard user interface
2. File cleanup functionality
3. Review approval capabilities
4. Notification system for user activities

### Managing Reviews

1. When a user submits a review, you'll receive a notification with their message
2. You can approve the review by clicking the "Опубликовать" button
3. Once approved, the review will be visible to all users
4. You'll receive confirmation when the review is published

### Data Management

The "Очистка файлов" button allows admins to reset the following data:
- Transaction history
- Review permissions
- Approved and pending reviews

### Processing Transactions

1. You will receive notifications of new exchange requests with both detailed and formatted versions
2. Contact users via their Telegram username
3. Follow standard exchange protocols for completing transactions

## User Guide

### Starting the Bot

1. Search for WireTransfer bot on Telegram
2. Click "Start" or type `/start`
3. You'll see the main menu with exchange options

### Checking Exchange Rates

1. Click "Курс" from the main menu
2. Current EUR/RUB rates will display:
   - RUB → EUR (buying euros)
   - EUR → RUB (selling euros)

### Requesting an Exchange

1. Click "Обмен" from the main menu
2. Select transaction type (Buy/Sell)
3. Choose your bank (Sberbank, Tinkoff, Raiffeisen)
4. Enter amount (minimum 10,000 RUB or 100 EUR)
5. Provide your IBAN
6. Enter your name and surname (Latin characters only)
7. Confirm your details
8. Wait for administrator contact

### Reading Instructions

Click "Инструкция" for detailed steps on the exchange process.

### Managing Reviews

1. Click "Отзывы" from the main menu
2. Options:
   - Write a review (only after completing a transaction)
   - Read approved user reviews
3. After submitting a review, it will be sent to administrators for approval
4. Once approved, your review will be visible to all users

## API Integration

WireTransfer integrates with the Central Bank of Russia API to obtain current exchange rates:

```python
def get_eur_rub():
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    if response.status_code == 200:
        data = response.json()
        eur_rub = data["Valute"]["EUR"]["Value"]
        return float(eur_rub)
    else:
        return None
```

Custom rates are calculated based on this data:
- Buy rate: CBR rate × 1.053
- Sell rate: CBR rate × 0.99

## Security

### Data Protection

- No sensitive financial data is stored long-term
- Message history cleanup prevents data exposure
- Input validation prevents injection attacks
- IBAN and name information for transaction purposes only

### Access Control

- Role-based permissions for admin functions
- Multi-step verification for critical operations
- Restricted review capabilities

## Data Management

### Storage System

WireTransfer uses four JSON files for data persistence:

1. `users_id.json`: Records multiple completed transactions with array storage
2. `users_id_review.json`: Tracks users who have submitted reviews
3. `reviews.json`: Stores approved user reviews
4. `reviews_confirm.json`: Stores pending reviews awaiting approval

### Data Formats

Example user storage format:
```json
{
  "user_ids": [123456789, 987654321, 456789123]
}
```

Example review storage format:
```json
{
  "123456789": ["✅ @username: Great service, fast exchange! Very satisfied.\n"]
}
```

## Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check your internet connection
   - Verify bot token is correct
   - Ensure Python script is running

2. **Can't write reviews**
   - You must complete a transaction first
   - You can only submit one review

3. **Exchange rate not showing**
   - Central Bank API may be temporarily unavailable
   - Check your internet connection

### Error Messages

- **"Сумма должна быть больше..."**: Minimum amount requirement not met
- **"Пожалуйста, введите имя и фамилию латиницей"**: Name must be in Latin characters
- **"Вы уже писали отзыв!"**: You've already submitted a review

## Contact & Support

For technical support or inquiries about WireTransfer:

- **Developer**: Aleksander Samarin
- **Location**: Blagoveshchensk, Russia
- **Year**: 2023
- **Contact**: @RSantila on Telegram

---

<p align="center">
  <strong>© 2023 Aleksander Samarin. All rights reserved.</strong><br>
  WireTransfer is provided for private use only. Redistribution or modification without explicit permission is prohibited.
</p>