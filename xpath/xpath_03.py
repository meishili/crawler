from lxml import etree
import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'https://www.aqistudy.cn/historydata/'

page_text = requests.get(url = url, headers = headers)

tree = etree.HTML(page_text)

# host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
# all_city_names = []
# for li in host_li_list:
#     host_city_name = li.xpath('./a/text')[0]
#     all_city_names.append(host_li_list)

# all_li_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
# for li in host_li_list:
#     host_city_name = li.xpath('./a/text')[0]
#     all_city_names.append(host_li_list)
# print(all_city_names, len(all_city_names))



