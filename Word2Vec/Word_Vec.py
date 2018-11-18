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
# 学習の実行
# ------------------------------------ #

txtfile = "public_text_splited.txt"

sentences = word2vec.LineSentence(txtfile)          # 分かち書きした文章の読み込み
model = word2vec.Word2Vec(sentences,                # ベクトル化のオプション設定
                          sg = 1,                   # 0: CBOW, 1: skip-gram
                          size = 300,               # ベクトルの次元数、default is 100
                          window = 5,               # 入力単語からの最大距離、default is 5
                          sample = 1e-3,            # 単語を無視する際の頻度のしきい値、default is 1e-3, useful range is (0, 1e-5)
                          alpha = 0.025,            # 学習率、default is 0.025 for skip-gram and 0.05 for CBOW
                          min_count = 1,            # 単語の出現回数でフィルタリング、学習に使う単語の最低出現回数、1で全て利用
                          )

model.save("word2vec.gensim.model")                 # モデルの保存


# ------------------------------------ #
# 作成したモデルの読み込み
# ------------------------------------ #

model_path = "word2vec.gensim.model"
model2 = word2vec.Word2Vec.load(model_path)

# ------------------------------------ #
# 学習結果からの判定処理
# ------------------------------------ #

w2vres = model2.most_similar(positive = '組み合わせ', topn = 10)
                                                    # 指定した単語と似ている単語を指定した上位数分抽出、距離の近さはコサイン類似度で計算
#pprint.pprint(w2vres)                               # 結果をプリントする

for x in w2vres:
    print(x[0], x[1])

# 別の#表現方法
#pprint.pprint(word2vec_model.most_similar(positive=['女', '国王'], negative=['男']))
                                                    # Word2Vecによる言葉の計算（例：女 + 国王 - 男）
# 単純な１単語間に類似度を算出したい場合は、model.similarityで計算できる
#print("類似度：", model2.similarity('猫', "人間"))
