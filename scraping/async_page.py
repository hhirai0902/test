from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# ------------------------------------ #
# 初期値設定
# ------------------------------------ #
# アクセスするURL
url = "http://yoheim.net/work/async_page.html"
#url = "https://www.footlocker.com/product/nike-free-m-2018--mens/42836008.html"


# PhantomJSをSelenium経由で利用します.
#driver = webdriver.PhantomJS()
# ブラウザを起動する
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

# 該当ページを取得＆レンダリングします
#driver.get("http://yoheim.net/work/async_page.html")
# ブラウザでアクセスする
driver.get(url)

# ちょっと待つ
# （ページのJS実行に時間が必要あれば）
# time.sleep(5) # 5s

# レンダリング結果をPhantomJSから取得します.
html = driver.page_source
# HTMLを文字コードUTF-8に変換して取得
html = driver.page_source.encode("utf-8")


# 画像のURLを取得する（JSでレンダリングしたところ）.
bs = BeautifulSoup(html, "html.parser")
img_urls = [img.get("src") for img in bs.select("#imageRoot img")]
pprint(img_urls)

# ついでにスクリーンショットも取れます.
driver.save_screenshot("ss.png")

# 終了
driver.quit()