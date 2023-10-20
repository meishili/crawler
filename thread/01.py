import requests
from lxml import etree
import random
import json
from multiprocessing.dummy import Pool

def get_video_data(dic):
    url = dic['url']
    # print(dic['name'], 'start!')
    print(url)
    data = requests.get(url = url, headers = headers).content
    print(url)
    with open(dic['name'], 'wb') as fp:
        fp.write(data)
        print(dic['name', 'download!'])

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'https://www.pearvideo.com/category_1'

page_text = requests.get(url = url, headers = headers).text
tree = etree.HTML(page_text)

li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
for li in li_list:
    detail_url = 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0]
    video_id = li.xpath('./div/a/@href')[0][6:]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    print(detail_url)
    # detail_page_text = requests.get(url = detail_url, headers = headers).text
    xhr_url = 'https://www.pearvideo.com/videoStatus.jsp'
    a = random.randint(0,1)
    data = {
        'contId': video_id,
        'mrd': str(a),
    }

    header = {
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'Host': 'www.pearvideo.com',
        'Referer': 'https://www.pearvideo.com/' + li.xpath('./div/a/@href')[0],
    }
    urls = []
    video_json = requests.post(url = xhr_url, headers = header, data = data).json()
    src = video_json['videoInfo']['videos']['srcUrl']
    # video_data = requests.get(url = src, headers = headers).content
    video_path = './video/' + name
    dic = {
        'name': video_path,
        'url': src
    }
    urls.append(dic)
    # get_video_data(dic)
    # with open(video_path, 'wb') as fp:
    #     fp.write(video_data)


pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()
