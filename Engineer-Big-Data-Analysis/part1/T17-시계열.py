# 2022년 5월 sales의 중앙값을 구하시오

# 데이터셋 : basic2.csv
# 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")

df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
con = (df['year'] == 2022) & (df['month'] == 5)

result = df[con]['Sales'].median()
print(result)

# 2022년 5월 sales의 중앙값을 구하시오
# 데이터셋 : basic2.csv

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day

con = (df['year'] == 2022) & (df['month'] == 5)
df = df[con]
df.head()
print(df['Sales'].median())

# 정답 : 1477685.0