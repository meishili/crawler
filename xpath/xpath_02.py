from lxml import etree
import requests
import os

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'https://pic.netbian.com/4kmeinv/'

response = requests.get(url = url, headers = headers)
# response.encoding = 'utf-8'
page_text = response.text

tree = etree.HTML(page_text)

li_list = tree.xpath('//div[@class="slist"]/ul/li')
if not os.path.exists('piclibs'):
    os.mkdir('piclibs')
for li in li_list:
    img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
    img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    print(img_src, img_name)

    img_data = requests.get(url = img_src, headers = headers).content
    img_path = 'piclibs/' + img_name
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name + 'downloda!')