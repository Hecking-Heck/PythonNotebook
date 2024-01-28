# Import
from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

# Display Homepage
@app.route("/")
def refreshCoins():
    crypto_coins = ['bitcoin','ethereum','litecoin','dogecoin']
    prices = fetch_crypto_prices(crypto_coins)
    display_prices(prices)

    return render_template("index.html", coins = prices)

def fetch_crypto_prices(coins):
    crypto_data = {}
    for coin in coins:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            crypto_data[coin] = data[coin]['usd']
        else:
            print(f"Failed to fetch data for {coin}")
    return crypto_data

def display_prices(prices):
    for coin, price in prices.items():
        print(f"{coin.capitalize()}: ${price}")

# Run app
if __name__ == "__main__":
    app.run(debug=True)