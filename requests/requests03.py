import requests
import json
post_url = 'https://fanyi.baidu.com/sug'

word = input('Enter a word:')

data = {
    'kw' : word
}

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

response = requests.post(url = post_url, data = data, headers = header)
dic_obj = response.json()
print(dic_obj)
fp = open(word + '.json', 'w', encoding = 'utf-8')
json.dump(dic_obj, fp = fp, ensure_ascii = False)
print("over!")
