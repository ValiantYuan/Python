import requests
keyWord = "Python"
kv = {'wd':keyWord}
url = "http://www.baidu.com/s"
try:
    r = requests.get(url, params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    r.encoding = r.apparent_encoding

except:
    print('爬取失败')
