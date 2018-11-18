# coding: UTF-8
# ------------------------------------ #
# インポートモジュール
# ------------------------------------ #
import urllib.request, urllib.error     # URL操作
from bs4 import BeautifulSoup           # htmlを読み込む
import re                               # 正規表現処理
import csv                              # CSVファイル操作
import requests                         # urlを読み込む
import os                               # フォルダ作成
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint


import uuid                             # ユニークなIDを生成

# ------------------------------------ #
# 初期値設定
# ------------------------------------ #
# アクセスするURL
#url = "file:///C:/Users/002048.FAS/Documents/hirai/trunk/as-raserver_work/python_script/Github/scraping/nikkeiheikin.html"
#url = "https://www.footlocker.com/product/nike-free-m-2018--mens/42836008.html"
#url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
#keyword = "猫"
url = "https://nico3shop.fashionstore.jp/items/13191495"


# ------------------------------------ #
# スクレイピング処理
# ------------------------------------ #
# ブラウザのオプションを格納する編集を取得
options = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが立ち上がる）
#options.set_headless(True)

# ブラウザを起動する
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", chrome_options = options)

# ブラウザでアクセスする
driver.get(url)

# HTMLを文字コードUTF-8に変換して取得
#html = driver.page_source.encode("utf-8")
# レンダリング結果をChromeから取得します。
html = driver.page_source

# URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
#html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う,URL内を解析
soup = BeautifulSoup(html, "html.parser")

# idがheikinの要素を表示
#print(soup.select_one("img"))


# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます
#imgs = soup.find_all("img")

#格納フォルダ作成
picfolder = "./picture"             # 画像格納フォルダ
if not os.path.isdir(picfolder):   # フォルダが存在していない場合
    os.mkdir("./picture")           # フォルダを作成する
else:                               # フォルダが存在している場合
    pass                            # なにもしない

# 取得
img_urls1 = soup.find_all("img")
# [`式` for `任意の変数名` in `イテラブルオブジェクト`]
# リストやタプルなどのイテラブルオブジェクトの各要素に対して式が評価され、その結果が要素となる新たなリストが返される。
img_urls2 = [img.get("src") for img in soup.select("img")]
img_urls2 = list(set(img_urls2))
#pprint(img_urls2)

images = []  # 画像リストの配列

# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
# imgがstrなのでif文が実行できない！！！
for img in img_urls1:
    if img.get("src").endswith(".jpg"):
        images.append(img.get("src"))  # imagesリストに格納
#        result = requests.get(img["src"])
    elif img.get("src").endswith(".png"):
        images.append(img.get("src"))  # imagesリストに格納
#        result = requests.get(img["src"])
    print(img["src"])

    for target in images:  # imagesからtargetに入れる
        re = requests.get(target)
        with open('./picture/' + target.split('/')[-1], 'wb') as f:  # imgフォルダに格納
            f.write(re.content)  # .contentにて画像データとして書き込む

    print("ok")  # 確認

