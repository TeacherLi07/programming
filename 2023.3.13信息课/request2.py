import requests
url='http://cba.sports.sina.com.cn/cba/stats/playerstats/?qleagueid=210&qround=0'
html=requests.get(url)    
html.encoding='gbk'
#print(html.text)               

from bs4 import BeautifulSoup

sp=BeautifulSoup(html.text,'html.parser')
b=[]
th=sp.find_all("th")
for i in th:
    b.append(i.text)
#print(b)

a=[]
u=[]
td=sp.find_all("td")
for i in td:
    a.append(i.text)
    if len(a) == 18:
        u.append(a)
        a=[]

import csv
with open(file='cba.csv',mode='w',encoding='gbk')as f:
    write=csv.writer(f)
    write.writerow(b)
    write.writerows(u)


   
