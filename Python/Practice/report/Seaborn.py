import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# データを取得 sampleDate使用
tips = sns.load_dataset("tips")
# 初めの5行表示
tips.head()

# ヒストグラム作成
sns.distplot(tips ["total_bill"],bins = 16,color = "purple")

# 散布図と回帰曲線の作成
sns.jointplot(x= "total_bill",y="tip",data=tips, color="purple",kind="reg")

# データが昼と夜で分かれているためそれをだす
time_grouped_lunch = tips.groupby('time').get_group('Lunch')
time_grouped_lunch.head
# 夜
time_grouped_dinner = tips.groupby('time').get_group('Dinner')
time_grouped_dinner.head()

# Lunchの場合のtipとtotal bill
sns.set(style="darkgrid", color_codes=True)
lunch_cor = sns.jointplot(data=time_grouped_lunch, x='total_bill',y='tip',kind='reg',color='g')
lunch_cor.annotate(stats.pearsonr)
# 夜
sns.set(style="darkgrid", color_codes=True)
dinner_cor = sns.jointplot(data=time_grouped_dinner, x='total_bill',y='tip',kind='reg',color='r')
dinner_cor.annotate(stats.pearsonr)

# 表示
plt.show()