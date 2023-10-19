import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
page_text = requests.get(url = url, headers = headers).text

soup = BeautifulSoup(page_text, 'lxml')

fp =  open('sanguoyanyi.html', 'w', encoding= 'utf-8')

li_list = soup.select('.book-mulu > ul > li')
for li in li_list:
    title = li.a.string
    # title = title.encode('iso-8859-1').decode('gbk')
    detail_url = 'http://www.shicimingju.com' + li.a['href']
    detail_pate_text = requests.get(url = detail_url, headers = headers).text
    detail_soup = BeautifulSoup(detail_pate_text, 'lxml')
    div_tag = detail_soup.find('div', class_ = 'chapter_content')
    content = div_tag.text
    content = content.encode('iso-8859-1').decode('gbk')
    fp.write(title + ': ' + content + '\n')
    print(title, 'over!')
