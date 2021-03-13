import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


#データのインポート
tips=pd.read_csv("./data/tips.csv")

tips.head()#先頭の5行を表示
tips.info()

# 各棒のxの値
left=range(4)

# 曜日を取得
day=tips.day.value_counts().keys()

# 棒の高さ
height=tips.day.value_counts().values

# 棒グラフの表示
# leftで与えられたxの値を、tick_labelに代入されたdayの文字列で置き換えている
plt.bar(left,height,tick_label=day)

plt.show()

#円グラフを作ろう，自分で調べてみよう！

#後は，散布図とかヒストグラムとか色々操作してみよう

##pandasは，tips["label名"]，tips.label名　でそこの列が持ってこれるよ
