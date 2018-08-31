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

import uuid                             # ユニークなIDを生成

# ------------------------------------ #
# 初期値設定
# ------------------------------------ #
# アクセスするURL
url = "file:///C:/Users/002048.FAS/Documents/hirai/trunk/as-raserver_work/python_script/Github/scraping/nikkeiheikin.html"
#url = "https://www.footlocker.com/product/nike-free-m-2018--mens/42836008.html"
#url = "https://search.nifty.com/imagesearch/search?select=1&q=%s&ss=up"
#keyword = "猫"



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
html = driver.page_source.encode("utf-8")


# URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
#html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う,URL内を解析
soup = BeautifulSoup(html, "html.parser")

# idがheikinの要素を表示
print(soup.select_one("#heikin"))


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