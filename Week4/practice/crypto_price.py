import requests

# Example: Fetching Bitcoin price in USDT
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
response = requests.get(url)
data = response.json()

print(f"{data['symbol']} price is {data['price']}")