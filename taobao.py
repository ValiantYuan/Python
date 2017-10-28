import requests, re
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        re = request.get(url, timeout = 30)
        re.raise_for_status()
        re.encoding = re.apparent_encoding
        return re.text
    except:
        return ""
def parsePage(ilt, html):"view_price":"268.00"
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*\"', html)
        for i in range(len(plt):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append(price, title)
    except:
        print("")

def printGoodsList(ilt):
    pass

def main():
    goods = '阿迪达斯夹克'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=’
    inforlist = []
    for i in range(depth):
        try:
            url = start_url + goods + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue

    printGoodsList(infoList)

main()
