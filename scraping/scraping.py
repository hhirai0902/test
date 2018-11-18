import os
import sys
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


from time import time, sleep
from urllib.request import urlopen, Request
from mimetypes import guess_extension
import traceback

class Fetcher:
    def __init__(self, ua=''):
        self.ua = ua

    def fetch(self, url):
        req = Request(url, headers={'User_Agent': self.ua})
        try:
            with urlopen(req, timeout=3) as p:
                b_content = p.read()
                mime = p.getheader('Content-Type')
        except:
            sys.stderr.write('Error in fetching {}\n'.format(url))
            sys.stderr.write(traceback.format_exc())
            return None, None
        return b_content, mime


fetcher = Fetcher('Mozilla/5.0')#ユーザーエージェント
page_num = 20
dirname = "./picture"             # 画像格納フォルダ

#画像保存用フォルダ作成
if not os.path.exists(dirname):
    os.makedirs(dirname)

# ------------------------------------ #
# スクレイピング処理
# ------------------------------------ #
# ブラウザのオプションを格納する編集を取得
options = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが立ち上がる）
#options.set_headless(True)

#アクセスURLを指定
url = "https://search.yahoo.co.jp/image/search?p=%E8%A1%9B%E8%97%A4%E7%BE%8E%E5%BD%A9&oq=&ei=UTF-8&save=0"
url = "https://search.yahoo.co.jp/image/search;_ylt=A2RCAwcIa45bzjkAHwqU3uV7?p=%E6%9C%AC%E7%94%B0%E7%BF%BC&aq=-1&oq=&ei=UTF-8"
#url = "https://nico3shop.fashionstore.jp/items/13191495"
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", chrome_options = options)

#Chromeで該当ページを取得&レンダリングします
driver.get(url)

# HTMLを文字コードUTF-8に変換して取得
html = driver.page_source.encode("utf-8")



for i in range(page_num):
    #レンダリング結果をChromeから取得します。
    html = driver.page_source


    #画像のurlを取得する
    soup = BeautifulSoup(html, "html.parser")
    img_urls = [img.get("src") for img in soup.select("img")]
    #img_urls = [img.get("href") for img in bs.find_all("a", target="img")]
    #img_urls.remove("javascript:void(0);")
    img_urls = list(set(img_urls))      # list:リスト格納、set：集合を表すデータ型
    #画像を保存する
    for j, img_url in enumerate(img_urls):
        sleep(0.1)
        img, mime = fetcher.fetch(img_url)
        if not mime or not img:
            continue
        ext = guess_extension(mime.split(';')[0])
        if ext in ('.jpe', '.jpeg'):
            ext = '.jpg'
        if not ext:
            continue
        result_file = os.path.join(dirname, str(i) + '_' + str(j) + ext)
        with open(result_file, mode='wb') as f:
            f.write(img)
        print('fetched', img_url)

    #次のページに移動する
    #driver.find_element_by_link_text('次へ>').click()

driver.quit