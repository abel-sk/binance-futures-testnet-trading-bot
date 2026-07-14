# Binance Futures Testnet Trading Bot

## Overview

This project is a Python command-line application that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**.

It uses the `python-binance` library and follows a modular structure with separate components for client management, order placement, validation, and logging.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command-line interface using `argparse`
- Input validation
- Logging to both console and log file
- Exception handling
- Environment variables using `.env`

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

## Requirements

- Python 3.x
- Binance Futures Testnet Account
- Binance Testnet API Key and Secret

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading_bot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

Example SELL MARKET order:

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

## Logging

Application logs are stored in:

```text
logs/trading_bot.log
```

The log file records:

- API requests
- API responses
- Errors

---

## Assumptions

- The application uses Binance Futures Testnet.
- API credentials are stored in a `.env` file.
- LIMIT orders require a price.
- MARKET orders do not require a price.

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging
