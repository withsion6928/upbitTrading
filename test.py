# import requests
#
# url = "https://api.upbit.com/v1/market/all"
#
# querystring = {"isDetails":"false"}
#
# headers = {"Accept": "application/json"}
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
#
# import os
# import jwt
# import uuid
# import hashlib
# from urllib.parse import urlencode
#
# import requests
# import threading
# import time
# def account_loop():
#
#     while True:
#         time.sleep(1)
#         access_key = "E3wOBHPIBxGRDamvPWXIDtQ7C1RMgLvMrfo9p0wc"
#         secret_key = "kfAKqq9T8MrlKvulqBIgzbxLGzMBZpdl6yOTGtTF"
#         server_url = "https://api.upbit.com"
#
#         payload = {
#             'access_key': access_key,
#             'nonce': str(uuid.uuid4()),
#         }
#
#         jwt_token = jwt.encode(payload, secret_key)
#         authorize_token = 'Bearer {}'.format(jwt_token)
#         headers = {"Authorization": authorize_token}
#
#         res = requests.get(server_url + "/v1/accounts", headers=headers)
#
#         print(res.json())
#
# threading.Thread(target=account_loop).start()
#
# while True:
#     time.sleep(1)
#     print("이후 코딩 실행 실시간 틱봉 수신")
#     res = requests.get("https://api.upbit.com/v1/ticker?markets=KRW-BTC")
#     print(res.json())