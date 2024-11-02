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

import requests

def fetch_webpage_safely():
    url = "https://www.ntu.edu.tw/"  # Example URL from your code
    
    try:
        # Use requests instead of urllib.request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Get the webpage content with proper encoding
        data = response.text
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

def main():
    webpage_content = fetch_webpage_safely()
    if webpage_content:
        print("Successfully retrieved webpage content")
        # Process the webpage_content as needed
    else:
        print("Failed to retrieve webpage content")

if __name__ == "__main__":
    main()
    