import requests

headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
url = 'https://www.sogou.com/web'
kw = input('Enter a word:')
param = {
    'query' : kw
}

response = requests.get(url = url, params = param, headers = headers)

page_text = response.text
filename = kw + '.html'
with open(filename, 'w', encoding = 'utf-8') as fp:
    fp.write(page_text)
print(filename, 'close!')