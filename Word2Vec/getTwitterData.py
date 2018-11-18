#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
import json
import requests
from requests_oauthlib import OAuth1
import re
import os

#取得したkeyを定義
access_token = '379567135-BJmz4A1CkBrdz76IbsPJRdilWj1jgodVgQeDoBAa'
access_token_secret = '62tuwaCpdzBiTuS7t5odcyKfcjECUPX0WdHzD3aOkTbLe'
consumer_key = 'E6QO1Kow4QCLR9rDlSD9aFD2F'
consumer_key_secret = 'qqAQaVe7e06DjvRCkOaIL8w6ljMlsXMdHSjUzjU6MtWCoTuLS3'

url = "https://stream.twitter.com/1.1/statuses/sample.json?language=ja"

def normalize_text(text):
    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text = re.sub('RT', "", text)
    text = re.sub('お気に入り', "", text)
    text = re.sub('まとめ', "", text)
    text = re.sub(r'[!-~]', "", text)
    text = re.sub(r'[︰-＠]', "", text)
    text = re.sub('\u3000',"", text)
    text = re.sub('\t', "", text)
    text = text.strip()
    return text

# OAuth で GET
auth = OAuth1(consumer_key, consumer_key_secret, access_token, access_token_secret)



# テキスト出力ファイルを開く
tsvfile = "public_text_twitter.tsv"  # 処理状況出力テキストファイル
if not os.path.exists(tsvfile):  # ファイルが存在していない場合
    f = open(tsvfile, mode="a", encoding='utf-8')  # テキストファイルを開く
else:  # ファイルが存在している場合、
    os.remove(tsvfile)  # 元のファイルを削除
    f = open(tsvfile, mode="a", encoding='utf-8')  # テキストファイルを開く

# テストを取得する
res = requests.get(url, auth=auth, stream=True)
for r in res.iter_lines():
    try:
        r_json = json.loads(r)
        text = r_json['text']
        f.write(normalize_text(text) + '\n')
    except:
        continue