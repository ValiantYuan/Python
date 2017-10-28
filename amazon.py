import requests
kv = {'user-agent':'Mozilla/5.0'}
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    print(r.encoding)
    print(r.apparent_encoding)
    print(r.headers)
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬取失败')
