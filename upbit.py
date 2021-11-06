import time

import pyupbit

access_key = "MP4SfTaJM8xywcxOEzKyxq9rLitoPdxrJrue7jrB"
secret_key = "Oyp1TN8VqRFxBNc97xZo9MUpmnT3f0X7PxHrfyT4"
upbit = pyupbit.Upbit(access_key, secret_key)
print(upbit.get_balances())

ticker = pyupbit.get_tickers(fiat="KRW")
print(ticker)

df = pyupbit.get_ohlcv("KRW-BORA")
print(df)

for i in ticker:
    time.sleep(1)
    print("%s : %s " % (i, float(pyupbit.get_current_price(i))))




# ret = upbit.sell_limit_order("KRW-BORA", 300, 20)
# print(ret)
