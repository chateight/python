import requests
from bs4 import BeautifulSoup
import re

site = requests.request('get', 'https://nikkei.com')
data = BeautifulSoup(site.text, "html.parser")

# dataオブジェクトはstr形式ではないから、dataオブジェクト(elem)に正規表現マッチングを直接は使えない
# 必要ならstr()でキャストする
elem = data.find_all(href=re.compile('nikkei.com/opinion'))
set = []
for ele in elem:
    set.append(ele.text)
set.sort()
set_uni = []
prev = ''
for item in set:
    if prev != item:
        set_uni.append(item)
        prev = item
print(set_uni)
