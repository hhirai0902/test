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

import uuid                             # ユニークなIDを生成

# ------------------------------------ #
# 初期値設定
# ------------------------------------ #
# アクセスするURL
url = "https://www.footlocker.com/product/nike-free-m-2018--mens/42836008.html"
#url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
keyword = "猫"

# 取得画像格納
images = []


# ------------------------------------ #
# スクレイピング処理
# ------------------------------------ #
# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
#html = urllib.request.urlopen(url%(keyword))
r = requests.get(url)

# htmlをBeautifulSoupで扱う,URL内を解析
#soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(r.content, "lxml")

# span要素全てを摘出する→全てのspan要素が配列に入ってかえされます
imgs = soup.find_all("img")

#格納フォルダ作成
picfolder = "./picture"             # 画像格納フォルダ
if not os.path.isdir(picfolder):   # フォルダが存在していない場合
    os.mkdir("./picture")           # フォルダを作成する
else:                               # フォルダが存在している場合
    pass                            # なにもしない


# for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
for img in imgs:
    if img.get("src").endswith(".jpg"):
        r = requests.get(img["src"])
    elif img.get("src").endswith(".png"):
        r = requests.get(img["src"])
    print(img["src"])
    with open(str("./picture/") + str(uuid.uuid4()) + str(".jpg"), "wb") as file:
        file.write(r.content)

