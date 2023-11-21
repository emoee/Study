# 주어진 데이터에서 2022년 5월 주말과 평일의 sales컬럼 평균값 차이를 구하시오 (소수점 둘째자리까지 출력, 반올림)
# 데이터셋 : basic2.csv

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['dayofweek'] = df['Date'].dt.dayofweek # 평일과 주말 나누기

con = (df['year'] == 2022) & (df['month'] == 5)
df = df[con]
day = (df['dayofweek'] < 5)

weekday = df[day]['Sales'].mean()
weekend = df[~day]['Sales'].mean()
print(round(weekend - weekday, 2))