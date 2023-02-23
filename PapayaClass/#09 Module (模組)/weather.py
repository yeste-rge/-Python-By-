#Python 零基礎新手入門 #09 Module (模組)
import requests

城市 = input("请输入城市名称:")
API = "c818e999b0f4658b4e406c4842c08eeb"
网址 = f"https://api.openweathermap.org/data/2.5/weather?q={城市}&appid={API}"
天气资料 = requests.get(网址)
气温 = int(天气资料.json()["main"]["temp"]-273.15)#json语法把这些资料转成⌈字典⌋一旦转成了⌈字典⌋ 我们就可以借由字典⌈标题⌋的输入来取得想要的资料
print(f"{城市}目前的气温是{气温}度")