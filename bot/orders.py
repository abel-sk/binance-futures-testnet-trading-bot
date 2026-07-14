from binance.exceptions import BinanceAPIException

from bot.client import get_client
from bot.logging_config import setup_logger

logger = setup_logger()


def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        logger.info(
            f"Sending MARKET order | Symbol={symbol} Side={side} Qty={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

        logger.info(
            f"OrderID={order.get('orderId')} "
            f"Status={order.get('status')} "
            f"ExecutedQty={order.get('executedQty')}"
        )

        return order

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        logger.info(
            f"Sending LIMIT order | Symbol={symbol} Side={side} Qty={quantity} Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )

        logger.info(
            f"OrderID={order.get('orderId')} "
            f"Status={order.get('status')} "
            f"ExecutedQty={order.get('executedQty')}"
        )

        return order

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise