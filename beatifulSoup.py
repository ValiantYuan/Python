import requests
from bs4 import BeautifulSoup

try:
    r = requests.get("http://python123.io/ws/demo.html")
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    print(soup.a.attrs)
except:
    print("链接无法获取")
