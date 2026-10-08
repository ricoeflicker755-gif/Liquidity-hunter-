# Liquidity Hunter FX

from market_data import get_market_data


def liquidity_hunter():
    print("Liquidity Hunter FX is running...")
    get_market_data()
    print("Analyzing liquidity and market structure...")
    print("System ready.")


if __name__ == "__main__":
    liquidity_hunter()
