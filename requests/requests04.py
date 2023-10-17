import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type' : '24',
    'interval_id' : '100:90',
    'action' : '',
    'start' : '0',
    'limit' : '20',
}

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

response = requests.get(url = url, params = param, headers = header)
list_data = response.json()
fp = open('douban.json', 'w', encoding = 'utf-8')
json.dump(list_data, fp = fp, ensure_ascii = False)
