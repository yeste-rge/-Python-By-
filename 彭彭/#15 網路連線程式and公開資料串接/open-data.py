#载入模组 import urllib.request 
#下载特定网址资料
#import urllib.request as request #别名叫做request
#with request.urlopen(网址)as response: 
#request.urlopen在这个地方放我们想要连线的网址，例如https.com在这个地方放我们想要连线的网址 python就会帮我们连线
#然后给我们一个response文件
#     data=response.read() #接着在with的区块中用这个response来读取这一个网址的资料那他一次呢就会把所有的资料都进来
#print(data)##然后我们把资料印出来

#网络连线
#import urllib.request as request
#src="https://nus.edu.sg/"
#src="https://www.ntu.edu.tw/"
#with request.urlopen(src) as response:
    #data=response.read().decode("utf-8") #取得网站的原始码 (HTML、CSS、JS)
#print(data)
#串接、截取公开资料
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/04a9e3ca-9d96-4f2a-aaef-ead33af206e5?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) #利用 json 模组处理 json 资料格式
    # 将公司名称列表出来
    clist=data["result"]["results"]
    with open("data.txt","w",encoding="utf-8") as file:
        for company in clist:
          file.write(company["免費接駁車路線"]+"\n")
