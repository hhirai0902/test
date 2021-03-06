# coding: UTF-8
# ------------------------------------ #
# インポートモジュール
# ------------------------------------ #
#import urllib2 # for python2.x
import urllib.request, urllib.error     # URL操作
from bs4 import BeautifulSoup           # スクレイピング
from datetime import datetime           # 日付時間データ操作
import csv                              # エクセルCSV
import time                             # 実行時間計測

# ------------------------------------ #
# 初期値設定
# ------------------------------------ #
# アクセスするURL
url = "https://www.nikkei.com/markets/kabu/"

# フラグ設定
time_flag = True

# 取得文字列格納
nikkei_heikin = ""


# ------------------------------------ #
# カウント関数
# ------------------------------------ #
def stub(i):
    print("{}回目の処理です。".format(i))


# ------------------------------------ #
# 繰り返し処理
# ------------------------------------ #
while True:
    # 時間が59分以外の場合は58秒間時間を待機する
    if datetime.now().minute != 16:
        # 59分ではないので1分(58秒)間待機します(誤差がないとは言い切れないので58秒です)
        time.sleep(15)
        continue        # 次のループ処理へ

    # csvを追記モード"a"で開きます→ここでcsvを開くのはファイルが大きくなった時にcsvを開くのに時間がかかるためです
    f = open("nikkei_heikin.csv", "a")
    writer = csv.writer(f, lineterminator = "\n")

    # 59分になりましたが正確な時間に測定をするために秒間隔で59秒になるまで抜け出せません
    while datetime.now().second != 59:
        # 00秒ではないので1秒待機
        time.sleep(1)
        print(datetime.now().second)
    # 処理が早く終わり二回繰り返してしまうのでここで一秒間待機します
    time.sleep(1)

    # csvに記述するレコードを作成します
    csv_list = []

    # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    # span要素全てを摘出する→全てのspan要素が配列に入ってかえされます
    # →[<span class="m-wficon triDown"></span>, <span class="l-miH02_H02c_btn_text">International</span>...
    # div:あらゆるものを挟んで大きなまとまりを作る、display:block
    # span:フレーズをグループ化する、グループしたフレーズはCSS（色設定など）を一括でできる、display:inline
    # class:divやspanに付ける名前
    span = soup.find_all("span")


    # for分で全てのspan要素の中からClass="mkc-stock_prices"となっている物を探します
    for tag in span:
        # classの設定がされていない要素は、tag.get("class").pop(0)を行うことのできないでエラーとなるため、tryでエラーを回避する
        try:
            # tagの中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
            # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
            # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
            string_ = tag.get("class").pop(0)

            # 摘出したclassの文字列にmkc-stock_pricesと設定されているかを調べます
            if string_ in "mkc-stock_prices":
                # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
                nikkei_heikin = tag.string
                # 摘出が完了したのでfor分を抜けます
                break
        except:
            # パス→何も処理を行わない
            pass

    # 現在の時刻を年、月、日、時、分、秒で取得します
    time_ = datetime.now().strftime("%Y %m %d %H:%M:%S")

    # 摘出した日経平均株価と時間を出力します。
    print(time_, nikkei_heikin)

    # 1カラム目に時間を挿入します
    csv_list.append(time_)

    # 2カラム目に日経平均を記録します
    csv_list.append(nikkei_heikin)

    # csvに追記します
    writer.writerow(csv_list)

    # ファイルの破損防止のために閉じます
    f.close()
