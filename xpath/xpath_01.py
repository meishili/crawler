from lxml import etree
import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'https://bj.58.com/ershoufang/'

page_text = requests.get(url = url, headers = headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="property"]')
fp = open('58.txt', 'w', encoding = 'utf-8')
for li in li_list:
    title = li.xpath('./a/div[2]/div/div/h3/text()')[0]
    print(title)
    fp.write(title + '\n')

