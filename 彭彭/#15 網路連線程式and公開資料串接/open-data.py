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

# Amazon Q
# The selected code is empty, so there is no specific problem to address.
# However, looking at the context, here are some potential improvements noted as comments:

# 1. The original code had commented-out sections using urllib.request
#    The code was improved by switching to the requests library which is more modern and easier to use

# 2. Error handling was added through try/except to handle network issues gracefully

# 3. A timeout was added to the request to prevent hanging

# 4. The code was structured into functions for better organization

# 5. Proper encoding handling was implemented using response.text instead of manual decoding

# 6. A main() function was added with proper __name__ == "__main__" check

# The current implementation is a good improvement over the original commented code