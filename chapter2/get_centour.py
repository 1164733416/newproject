import requests
from bs4 import  BeautifulSoup

url = "http://www.cntour.cn"
strhtml= requests.get (url)
soup=BeautifulSoup(strhtml.text ,'lxml')
data=soup.select('#footer')
print(data)


