import matplotlib.pyplot as plt
import numpy as np

#matplotlib inline #jupyter notebook が使いたい時は書いてね

# グラフのサイズの指定
plt.figure(figsize=(4,4))
# 引数に指定された値のプロット。引数として、描画する点のx座標, y座標の設定、凡例に表示する文字列の設定
plt.plot([0,2,4,6,8], [0,6,12,24,48],  label="graph")
# x, y軸のラベルの設定
plt.xlabel("x axis")
plt.ylabel("y axis")
# タイトルの設定
plt.title("title")
#　凡例の表示
plt.legend()
# グラフの出力
plt.show()

#ヒント
np.linspace(0,10,20)
