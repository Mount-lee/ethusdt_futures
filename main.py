from binance import Client
from datetime import datetime

api = 'rnyCGuKJnTrx2TmK2R4bJYvrmGZd3qG3enWPo5Y9RgkjM9QxesjcJ5VNCJaTR1ZW'
secret_key = 'H0diYMmh0crMHW77qlAALwD1g2XZRnDKHDTZNMFGFrRVY9QbNGZkbSPq66EHqtVT'
client = Client(api, secret_key)

klines = client.get_historical_klines('ETHUSDT', Client.KLINE_INTERVAL_1HOUR, '1 day ago UTC')

prices = []
times = []
i = 0
k = 1

for kline in klines:
    price = float(kline[4])
    time = datetime.fromtimestamp(kline[0] / 1000)
    prices.append(price)
    times.append(time)

for p in prices:
    if ((p[i] / p[k]) == 1.01 or (p[i] / p[k]) == 0.99) and i != 24:
        print("Цена ETH изменилась на 1% или более", p[i], '->', p[k])
        i += i
        k += k
