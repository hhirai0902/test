#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
import MeCab
import pandas as pd
import unicodedata
import os

#データ　インポート
tsvfile = 'wagahaihanekodearu.txt'                                 #tsvファイル：タブ区切りファイル
mecabpath = "C:/Program Files/MeCab/dic/mecab-ipadic-neologd"       # mecab-ipadic-neologdパス

df = pd.read_csv(tsvfile, names=['text'])                           # データをpandasでロードする

#df = pd.read_csv(open(tsvfile, 'rU'), sep='\t', names=['text'], encoding='utf-8_sig', engine='c')
# df = pd.read_csv(open(tsvfile, 'rU'), sep='\t', names=['text'], encoding='utf-8_sig', engine='c')
# sep:区切り文字の指定、\t:タブ文字
# names:任意の値を列名として指定、リストまたはタプルで指定する
# encoding:エンコーディングの指定、どフォルトはutf-8
# engine:{‘c’, ‘python’}, optional Parser engine to use. The C engine is faster while the python engine is currently more feature-complete.
text_lists = df['text'].unique().tolist()                           # ロードしたできすとをリストに格納する

#分かち書き
mt = MeCab.Tagger("-Ochasen") #自分がインストールした辞書を指定         # 分かち書き処理


# テキスト出力ファイルを開く
txtfile = "public_text_splited.txt"                                 # 処理状況出力テキストファイル
if not os.path.exists(txtfile):                                     # ファイルが存在していない場合
    f = open(txtfile, mode="a", encoding='utf-8')                   # テキストファイルを開く
else:                                                               # ファイルが存在している場合、
    os.remove(txtfile)                                              # 元のファイルを削除
    f = open(txtfile, mode="a", encoding='utf-8')                   # テキストファイルを開く

for text in text_lists:                                             # テキストリストを1つずつ処理
    tmp_lists = []                                                  # 新しいリスト作成
    text = unicodedata.normalize('NFKC',str(text))                  # 半角カタカナ、全角英数、ローマ数字・丸数字、異体字などなどを正規化
                                                                    # K：半角カタカナなどを正規化、D：ガギグゲゴのカと”に分ける
    if 'まじ卍' in text:
        text = text.replace('まじ卍','マジ卍')
    if 'マジ卍' in text:
        text_splited = text.split('マジ卍')
        for i, text in enumerate(text_splited):

            node = mt.parseToNode(text)
            while node:
                if node.feature.startswith('名詞') or node.feature.startswith('形容詞'):
                    tmp_lists.append(node.surface)
                node = node.next
            if i != len(text_splited)-1:
                tmp_lists.append('マジ卍')
    else:
        node = mt.parseToNode(text)
        while node:
            if node.feature.startswith('名詞') or node.feature.startswith('形容詞'):
                tmp_lists.append(node.surface)
            node = node.next
    f.write(' '.join(tmp_lists) + '\n')