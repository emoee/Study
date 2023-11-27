# 1-1. age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력¶
import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

q1 = df['age'].quantile(0.25)
q3 = df['age'].quantile(0.75)

import numpy as np
result = np.floor(abs(q3 - q1))
print(int(result))

# 1-2.(loves반응+wows반응)/(reactions반응) 비율이 0.4보다 크고 0.5보다 작으면서, type 컬럼이 'video'인 데이터의 갯수
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/fb.csv")

one = ((df['loves'] + df['wows'])/df['reactions']) > 0.4
two = ((df['loves'] + df['wows'])/df['reactions']) < 0.5
three = df['type'] == 'video'
result = df[one & two & three]

print(len(result))

# 1-3. date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification-kr-2022/nf.csv")
df['date_added'] = pd.to_datetime(df['date_added'])
df['year'] = df['date_added'].dt.year
df['mon'] = df['date_added'].dt.month

con1 = (df['year'] == 2018) & (df['mon'] == 1)
con2 = (df['country'] == 'United Kingdom')

result = df[con1 & con2]
print(len(result))