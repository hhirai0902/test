#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')         # 該当ワーニングを表示しないようにする
warnings.filterwarnings(action='ignore', category=FutureWarning, module='gensim')       # 該当ワーニングを表示しないようにする

from gensim.models import word2vec
import logging
import sys

# ------------------------------------ #
# 作成したモデルの読み込み
# ------------------------------------ #

model_path = "word2vec.gensim.model"
model = word2vec.Word2Vec.load(model_path)



# ------------------------------------ #
# 学習結果からの判定処理（加減対応）
# ------------------------------------ #
def neighbor_word(posi, nega=[], n=10):
    count = 1
    result = model.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        print(str(count)+" "+str(r[0])+" "+str(r[1]))
        count += 1

def calc(equation):
    if "+" not in equation or "-" not in equation:
        neighbor_word([equation])
    else:
        posi,nega = [],[]
        positives = equation.split("+")
        for positive in positives:
            negatives = positive.split("-")
            posi.append(negatives[0])
            nega = nega + negatives[1:]
        neighbor_word(posi = posi, nega = nega)

if __name__=="__main__":
    equation = sys.argv[1]
    calc(equation)
