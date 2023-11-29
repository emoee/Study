# 문제1

# 데이터셋(basic1.csv)의 'f5' 컬럼을 기준으로 상위 10개의 데이터를 구하고,
# 'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후,
# 'age'컬럼에서 80 이상인 데이터의'f5 컬럼 평균값 구하기

# 라이브러리 및 데이터 불러오기
import pandas as pd

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df.head()

df = df.sort_values('f5', ascending=False)
df_min = df['f5'].head(10).min()

df.iloc[:10,-1] = df_min

con = (df['age'] >= 80)
result = df[con]['f5'].mean()
print(result)

# 문제2

# 데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
# 'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
# 두 표준편차 차이 계산하기

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

df = df[:(int(len(df) * 0.7))]
result1 = df['f1'].std()
df['f1'] = df['f1'].fillna(df['f1'].median())
result2 = df['f1'].std()

result3 = (result1 - result2)
print(result3)

# 문제3

# 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
# 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
q = df['age'].std() * 1.5
m = df['age'].mean()

con1 = (df['age'] > q+m)
con2 = (m-q > df['age'])
result = df[con1 | con2]['age']
print(sum(result))