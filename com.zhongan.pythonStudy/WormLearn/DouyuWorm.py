import urllib.request
import string
import re
import json
import sys,os


url = "http://capi.douyucdn.cn/api/v1/getColumnRoom/8?offset="
urlAfter = "&limit=30&client_sys=android"
downLoadUrl = "D:\wormDownload\douyuworm\\"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

offset = 0
#下载张数
count = 1

#获取网页json
def getHtml(url):
    req = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html.decode("UTF-8")

#下载图片
def downLoadImg(url):
    file = open(downLoadUrl + url.split("/")[-1],'wb')
    req = urllib.request.Request(url=url, headers=headers)
    img = urllib.request.urlopen(req)
    buf = img.read()
    file.write(buf)
    return

#动态生成路径
def getLink(url):
    response = getHtml(url)
    response = response.encode('latin-1').decode('unicode_escape')
    jsonText = json.loads(response)
    #获取所有数据
    test = jsonText["data"]
    for i in test:
        src = i["vertical_src"]
        downLoadImg(src)
        global count
        print("已下载"+str(count)+"张"+src+"-*-"+str(offset))
        count = count + 1
    return

#动态修改offset获取更多图片
while(True):
    finalUrl = url + str(offset) + urlAfter
    getLink(url)
    offset = offset + 20
