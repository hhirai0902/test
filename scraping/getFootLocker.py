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
url = "https://www.nikkei.com/markets/kabu/"
#url = "https://www.footlocker.com/product/nike-free-m-2018--mens/42836008.html"
#url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
#keyword = "猫"



# ------------------------------------ #
# スクレイピング処理
# ------------------------------------ #
# URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
instance = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う,URL内を解析
soup = BeautifulSoup(instance, "html.parser")

# CSSセレクターを使って指定した場所のtextを表示します
print(soup.select_one("#CONTENTS_MARROW > div.mk-top_stock_average.cmn-clearfix > div.cmn-clearfix > div.mkc-guidepost > div.mkc-prices > span.mkc-stock_prices").text)


'''
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

'''