#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------ #
# モジュールの読み込み
# ------------------------------------ #
import numpy as np

# N次元配列を作成する
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print(x)

# N次元配列の型・サイズを確認する
# 配列自体の型を確認
print("type=", type(x))

# 配列の要素の型を確認
print("eletype=", x.dtype)

# 配列のサイズを確認
print("shape=", x.shape)

## Numpyで行列を操作する
# 配列の要素にアクセスする
# 特定の要素の値を取得
print(x[1,2])

# 0行目のみを取得
print(x[0])

