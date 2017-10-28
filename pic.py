import requests, os

url = "https://img11.360buyimg.com/mobilecms/s250x250_jfs/t4558/339/3558559326/85151/3b8c443a/58feab54Nc242b7ac.jpg"
root = "E://PythonCode//"
path = root + url.split('/')[-1]


try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as pic:
            pic.write(r.content)
            pic.close()
            print('图片保存成功')
    else:
        print('图片已存在')
except:
    print('爬取失败')
