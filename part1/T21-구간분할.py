# 나이 구간 나누기
# basic1 데이터 중 'age'컬럼 이상치를 제거하고, 동일한 개수로 나이 순으로 3그룹으로 나눈 뒤 각 그룹의 중앙값을 더하시오
# (이상치는 음수(0포함), 소수점 값)

import pandas as pd

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
con = (df['age'] <= 0)
df = df[~con]

df = df[(df['age'] == round(df['age'],0))] # 반올림 값과 원래의 값을 비교하여 동일하지 않으면 제외함.
df['range'] = pd.qcut(df['age'], q=3, labels=['1', '2', '3'])
df['range'].value_counts()
                      
df1 = df[(df['range'] == '1')]['age'].median()
df2 = df[(df['range'] == '2')]['age'].median()
df3 = df[(df['range'] == '3')]['age'].median()

print(df1 + df2 + df3)