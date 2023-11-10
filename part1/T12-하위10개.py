# %% [code]
# 주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구해보세요 
# (단, 100%가 넘는 접종률 제거, 소수 첫째자리까지 출력)

import pandas as pd
df = pd.read_csv("../input/covid-vaccination-vs-death/covid-vaccination-vs-death_ratio.csv")

df2 = df.groupby('country').max()
df2 = df2.sort_values(by='ratio', ascending = False)

cond = df2['ratio'] <= 100
df2 = df2[cond]

top = (df2['ratio'].head(10).mean())
bottom=(df2['ratio'].tail(10).mean())

print(round(top-bottom, 1))