#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import glob
import shutil
from time import sleep

# ブラウザのオプションを格納する編集を取得
options = Options()


# webdriverという仮想のブラウザを呼び出す
# browser = webdriver.PhantomJS()
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe", chrome_options = options)

# ログイン先のURLをセット
# loginUrl = "https://www.hatena.ne.jp/login"
loginUrl = "https://30d.jp/login"
# そのページにWebdriverをアクセスさせる
browser.get(loginUrl)

# ユーザーIDとパスワードの設定
# username = "hhide1234"
# password = "hidehide"
username = "dckqg730@yahoo.co.jp"
password = "wagon454"

# ------------------------------------ #
# フォルダ・アクセスアルバム設定
# ------------------------------------ #
dirname = "184"             # 画像格納フォルダ
files = 320                # ファイル数

#画像保存用フォルダ作成
basedownloadpath = "C:/Users/002048.FAS/Documents/hirai/trunk/Downloads"
if not os.path.exists(basedownloadpath + "/" + dirname):
    os.makedirs(basedownloadpath + "/" + dirname)
else:
    pass

# ---------------------------------------------------------------- #
# ログインページのフォームのid, class, もしくはxpathを取得する
# F12→ユーザーネームを選択→select→入力部を選択→ハイライト部でcopy→xpath
# ---------------------------------------------------------------- #
# ユーザーID入力部のxpath
# userNameField = browser.find_element_by_xpath("//*[@id='login-name']")
userNameField = browser.find_element_by_xpath("//*[@id='login_or_email']")
# データの挿入
userNameField.send_keys(username)

# パスワード入力部のxpath
# passwordField = browser.find_element_by_xpath("//*[@id='container']/div/form/div/div[2]/div/input")
passwordField = browser.find_element_by_xpath("//*[@id='password']")
# データの挿入
passwordField.send_keys(password)

# 送信するボタンのxpath
# submitButton = browser.find_element_by_class_name("submit-button")
submitButton = browser.find_element_by_xpath("//*[@id='submit_image']")
# クリック
submitButton.click()

# ページタイトルを表示
print(browser.title)

# アルバムページに移動
# profile = "http://30d.jp/himahimatan/" + dirname
# browser.get(profile)
# # ページタイトルを表示
# browser.title

# グローバル化
newlist = []
root = {}
ext = {}

# アルバム画像ページに移動
for file, name in enumerate(range(files), start=1):
    profile = "http://30d.jp/himahimatan/" + dirname + "/photo/" + str(file)
    browser.get(profile)
    # ページタイトルを表示
    browser.title


    # ダウンロードボタンのxpath
    # heading1 = browser.find_element_by_tag_name('h2')
    # if heading1 is "404 Error File Not Found":
    #     pass
    # else:
    try:
        # 要素がある場合の処理
        submitButton = browser.find_element_by_xpath("//*[@id='download']")
        # クリックしてダウンロード
        submitButton.click()
        sleep(3)
#        while len(newlist) <= 0:
        while True:         # 無限ループ
            # ディレクトリ直下のファイル一覧を取得
            filelist = glob.glob(basedownloadpath + "/*")
            # 該当文字が入ったファイル絶対パスをリストに格納
            newlist = [l for l in filelist if 'original' in l]
            basename = os.path.basename(newlist[0])  # ファイルパス取得
            root, ext = os.path.splitext(basename)  # 拡張子取得
            if ext in [""]:
                continue        # 次のwhile処理へ
            elif ext in [".crdownload"]:
                continue        # 次のwhile処理へ
            elif ext in [".jpg", ".JPG", ".jpeg", ".JPEG"]:
                # ファイル移動
                shutil.move(newlist[0], basedownloadpath + "/" + dirname + "/" + root + "_" + str(file) + ext)
                newlist = []
                break       # whileを抜ける
            else:
                continue        # 次のwhile処理へ
    except:
        # 要素がない場合の処理
        pass
