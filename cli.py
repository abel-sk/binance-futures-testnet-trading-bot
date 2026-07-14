import argparse

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def print_separator():
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print_separator()
        print("BINANCE FUTURES TESTNET TRADING BOT")
        print_separator()

        print("\nOrder Request")
        print("-" * 20)
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if order_type == "LIMIT":
            if args.price is None:
                raise ValueError("LIMIT orders require --price")

            price = validate_price(args.price)
            print(f"Price      : {price}")

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price,
            )

        else:
            response = place_market_order(
                symbol,
                side,
                quantity,
            )

        print("\nOrder Response")
        print("-" * 20)
        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Order Type     : {response.get('type')}")
        print(f"Side           : {response.get('side')}")
        print(f"Price          : {response.get('price')}")
        print(f"Average Price  : {response.get('avgPrice', 'N/A')}")
        print(f"Client OrderID : {response.get('clientOrderId')}")

        print("\nSUCCESS ✓ Order submitted successfully.")
        print_separator()

    except Exception as e:
        print("\nFAILED ✗")
        print(e)


if __name__ == "__main__":
    main()