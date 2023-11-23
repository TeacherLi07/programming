import requests
from bs4 import BeautifulSoup
url='http://cba.sports.sina.com.cn/cba/stats/playerstats/?qleagueid=210&qround=0'
html=requests.get(url)
html.encoding='utf-8'
sp=BeautifulSoup(html.text,'html.parser')
title=sp.select("title")
print(sp.title.text)
