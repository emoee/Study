# 주어진 데이터에서 2022년 월별 Sales 합계 중 가장 큰 금액과
# 2023년 월별 Sales 합계 중 가장 큰 금액의 차이를 절대값으로 구하시오.
# 단 Events컬럼이 '1'인경우 80%의 Salse값만 반영함
# (최종값은 소수점 반올림 후 정수 출력)

# 데이터셋 : basic2.csv

import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic2.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month

def eventsCheck(x):
    if x['Events'] == 1:
        return x['Sales'] * 0.8
    else:
        return x['Sales']

df['RSales'] = df.apply(eventsCheck, axis=1)

con2 = (df['year'] == 2022)
con3 = (df['year'] == 2023)

data2 = df[con2].groupby('month')['RSales'].sum().max()
data3 = df[con3].groupby('month')['RSales'].sum().max()

print(int(round(abs(data2-data3),0)))
# 정답 : 42473436