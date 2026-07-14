import os

from dotenv import load_dotenv
from binance.client import Client

from bot.logging_config import setup_logger

load_dotenv()

logger = setup_logger()


def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "API credentials not found. Please check your .env file."
        )

    logger.info("Connecting to Binance Futures Testnet...")

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True,
    )

    logger.info("Client created successfully.")

    return client