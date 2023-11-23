import requests
from bs4 import BeautifulSoup
url='http://cba.sports.sina.com.cn/cba/stats/playerstats/?qleagueid=210&qround=0'
requests.get(url).encoding='utf-8'
title=BeautifulSoup(requests.get(url).text,'html.parser').select("title")
print(title)
print(BeautifulSoup(requests.get(url).text,'html.parser').title.text)