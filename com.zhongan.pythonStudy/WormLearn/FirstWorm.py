import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    html = html.decode('utf-8')  # python3
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, 'D:\wormDownload\%s.jpg' % x)
        x += 1



html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))