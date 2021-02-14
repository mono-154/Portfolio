import math
import sys

import numpy
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/nkmk/tokyo-covid19-data-analysis/master/data/130001_tokyo_covid19_patients_20200731.csv')


# 元になるデータをコピー SettingWithCopyWarningの対処
df = df[['公表_年月日', '患者_年代', '退院済フラグ']].copy()

# renameで列名を変更
df.rename(columns={'公表_年月日': 'date_str', '患者_年代': 'age_org', '退院済フラグ': 'discharged'},inplace=True)

# isinで条件抽出　　~の使用でブール値を返し　Trueを反転して行を削除
df = df[~df['age_org'].isin(['不明', "'-"])]

# 日時の列　　インデックスをdatetime64[ns]型にし、時系列データの処理機能増加
df['date'] = pd.to_datetime(df['date_str'])

# 年代の区分
df['age'] = (
    df['age_org'].replace(['10歳未満', '10代'], '0-19')
    .replace(['20代', '30代'], '20-39')
    .replace(['40代', '50代'], '40-59')
    .replace(['60代', '70代', '80代', '90代', '100歳以上'], '60-')
)

# 年代のクロス集計
df_ct = pd.crosstab(df['date'], df['age'])
# 先ほどのdatetime64[ns]型に変換した列が新たなインデックスとなり、DatetimeIndexとして扱われるため　resampleで週ごとに集計
df_ct_week = df_ct.resample('W', label='left').sum()

# 棒グラフ作成
df_ct_week[:-1].plot.bar(stacked= True)

df_ct_week_str = df_ct_week.copy()
df_ct_week_str.index = df_ct_week_str.index.strftime('%Y-%m-%d')

df_ct_week_str[:-1].plot.bar(stacked=True, figsize=(8, 4))



plt.show()