from lxml import etree
import requests
import os
from chaojiying import Chaojiying_Client

def getCodeText(imgpath):
    chaojiying = Chaojiying_Client('13008724631', 'qisini741', '953677')	#用户中心>>软件ID 生成一个替换 96001
    im = open(imgpath, 'rb').read()	
    return chaojiying.PostPic(im, 1902)['pic_str']


headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

page_text = requests.get(url = url, headers = headers).text
tree = etree.HTML(page_text)

code_img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]

img_data = requests.get(url = code_img_src, headers = headers).content
with open('code.jpg', 'wb') as fp:
    fp.write(img_data)

code_text = getCodeText('code.jpg')
print(code_text)

