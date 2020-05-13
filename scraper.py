import urllib.request
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/FB?p=FB'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)

resp = urllib.request.urlopen(req)

html = resp.read()

soup = BeautifulSoup(html, 'html.parser')

tagged_values = soup.find_all("td", {'class': 'Ta(end) Fw(b)'})

values = []
for tv in tagged_values:
	tv.get_text()

# values = [x.get_text() for x in tagged_values]

for value in values:
	print(value)

print('/n')