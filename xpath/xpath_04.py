from lxml import etree
import requests
import os

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9&classID=864'

page_text = requests.get(url = url, headers = headers).text

tree = etree.HTML(page_text)

div_list = tree.xpath('//div[@id="main"]/div/div')



if not os.path.exists('pptxlibs'):
    os.mkdir('pptxlibs')
for li in div_list:
    div_src = 'https:' + li.xpath('./a/@href')[0]
    div_name = li.xpath('./a/img/@alt')[0] + ".pptx"
    down_text = requests.get(url = div_src, headers = headers).text
    down_tree = etree.HTML(down_text)
    down_scr = down_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li')[1]
    down_scr = down_scr.xpath('./a/@href')[0]
    data = requests.get(url = down_scr, headers = headers).content
    pptx_path = 'pptxlibs/' + div_name
    with open(pptx_path, 'wb') as fp:
        fp.write(data)
        print(div_name + 'downloda!')

