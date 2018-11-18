#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "hide"
PASS = "hidehide"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS,
    "back":"index.php",
    "mml_id":"0"
}

# action
url_login = "http://uta.pw/sakusibbs/users.php?action=login&amp;m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

print(res.text)
