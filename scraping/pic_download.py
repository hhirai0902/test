import requests
import re
import uuid
from bs4 import BeautifulSoup

url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
keyword = "猫"
r = requests.get(url%(keyword))
soup = BeautifulSoup(r.content,'lxml')
imgs = soup.find_all('img',src=re.compile('^https://msp.c.yimg.jp/yjimage'))
for img in imgs:
        print(img['src'])
        r = requests.get(img['src'])
        with open(str('./picture/')+str(uuid.uuid4())+str('.jpeg'),'wb') as file:
                file.write(r.content)