# Binance Futures Testnet Trading Bot

A Python command-line application that places **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)** using the official `python-binance` library.

---

## Features

- Place **MARKET** orders
- Place **LIMIT** orders
- Supports **BUY** and **SELL**
- Command-line interface using `argparse`
- Input validation
- Logging to console and log file
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
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
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

## Prerequisites

- Python 3.x
- Git
- Binance Futures Testnet Account
- Binance Futures Testnet API Key & Secret

---

## Installation

### Clone the repository

```bash
git clone https://github.com/abel-sk/binance-futures-testnet-trading-bot.git

cd binance-futures-testnet-trading-bot
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### Install dependencies

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

### Place a MARKET BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### Place a MARKET SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

---

### Place a LIMIT BUY Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

### Place a LIMIT SELL Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

---

## Sample Output

```text
==================================================
BINANCE FUTURES TESTNET TRADING BOT
==================================================

Order Request
--------------------
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001

Order Response
--------------------
Order ID       : 21641352796
Status         : NEW
Executed Qty   : 0.0000
Price          : 0.00
Average Price  : N/A

SUCCESS ✓ Order submitted successfully.
==================================================
```

---

## Logging

Logs are stored in:

```text
logs/trading_bot.log
```

Each request records:

- Request details
- Response details
- Errors (if any)

---

## Error Handling

The application handles:

- Invalid user input
- Missing API credentials
- Binance API exceptions
- Unexpected runtime errors

---

## Technologies Used

- Python 3
- python-binance
- python-dotenv
- argparse
- logging

## Architecture

The application is organized into separate modules:

- **client.py** – Creates and configures the Binance API client.
- **orders.py** – Contains the logic for placing MARKET and LIMIT orders.
- **validators.py** – Validates user input before sending requests.
- **logging_config.py** – Configures logging for console and file output.
- **cli.py** – Command-line entry point that processes user input and displays results.
---

## Assumptions

- Uses **Binance Futures Testnet (USDT-M)**.
- API credentials are stored in a `.env` file.
- MARKET orders do not require a price.
- LIMIT orders require a valid price.

---

## Author

**Abel Mathew Samson**

GitHub: https://github.com/abel-sk
