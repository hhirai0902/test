#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')         # 該当ワーニングを表示しないようにする
warnings.filterwarnings(action='ignore', category=FutureWarning, module='gensim')       # 該当ワーニングを表示しないようにする

from gensim.models import word2vec
import pprint

# ------------------------------------ #
# 作成したモデルの読み込み
# ------------------------------------ #

model_path = "word2vec.gensim.model"
model2 = word2vec.Word2Vec.load(model_path)

# ------------------------------------ #
# 判定テキストの読み込み
# ------------------------------------ #

judtxtfile = "judge.txt"

f = open(judtxtfile, 'r')  # ファイルを開く

# ファイル内テキストを取り出す #
posi = []
neg = []

for judtext in f:
    ### 最後の/で分割し格納 ###
    repos = reposold.rsplit("\\")   #右側から分割
    repos = repos[2].rstrip()    #後端の空白コード削除
    repos = repos.rstrip("\r\n")    #後端の改行コード削除


# ------------------------------------ #
# 学習結果からの判定処理
# ------------------------------------ #

w2vres = model2.most_similar(positive = '猫', negative = "人", topn = 10)
                                                    # 指定した単語と似ている単語を指定した上位数分抽出、距離の近さはコサイン類似度で計算
#pprint.pprint(w2vres)                               # 結果をプリントする

for x in w2vres:
    print(x[0], x[1])

# 別の#表現方法
#pprint.pprint(word2vec_model.most_similar(positive=['女', '国王'], negative=['男']))
                                                    # Word2Vecによる言葉の計算（例：女 + 国王 - 男）
# 単純な１単語間に類似度を算出したい場合は、model.similarityで計算できる
#print("類似度：", model2.similarity('猫', "人間"))
