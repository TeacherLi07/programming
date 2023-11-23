import requests
from bs4 import BeautifulSoup
import csv

url='http://cba.sports.sina.com.cn/cba/stats/playerstats/?qleagueid=210&qround=0'
html=requests.get(url)    
html.encoding='GBK'
sp=BeautifulSoup(html.text,'html.parser')
b=[]
th=sp.find_all("th")
for i in th:
    b.append(i.text)
    with open('title.txt',"a+") as f:
        f.write(i.text)
        f.write("\n")
        f.close
with open(file='cba.csv',mode='w',encoding='gbk') as f:
    write=csv.writer(f)
    write.writerow(b)
print(th)
print(b)
