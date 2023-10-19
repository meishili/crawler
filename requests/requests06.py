import requests

header = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = 'http://scxk.nmpa.gov.cn:81/xk/'

page_text = requests.get(url = url, headers = header).text
print(page_text)
with open('huazhuangpin.html', 'w', encoding = 'utf-8') as fp:
    fp.write(page_text)