import pandas as pd
import os

# データが格納されている作業ディレクトリまでパス指定
os.chdir("C:/Users/002048.FAS\Documents/hirai/trunk/as-raserver_work/python_script/Github/Word2Vec")
# csvの読み取り
df= pd.read_csv("public_text_twitter.tsv")
print(df)

