import requests
import json

url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
keyword = input("Enter city:")
pageIndex = input('Enter begin page:')
param = {
    'cname' : '',
    'pid' : '',
    'keyword' : keyword,
    'pageIndex' : pageIndex,
    'pageSize' : '10',
}

reponse = requests.get(url = url, data = param, headers = header)
list_data = reponse.text
# list_data =json.loads(list_data)
fp = open('kfc.html', 'w', encoding = 'utf-8')
print(list_data)
json.dump(list_data, fp = fp, ensure_ascii = False)
