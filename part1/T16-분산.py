# %% [code]
# 주어진 데이터 셋에서 f2가 0값인 데이터를 age를 기준으로 오름차순 정렬하고
# 앞에서 부터 20개의 데이터를 추출한 후 
# f1 결측치(최소값)를 채우기 전과 후의 분산 차이를 계산하시오 (소수점 둘째 자리까지)

# - 데이터셋 : basic1.csv 

import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
con = (df['f2'] == 0)
df = df[con].sort_values('age', ascending= True)
df = df[:20]

before = df['f1'].var()
df['f1'] = df['f1'].fillna(df['f1'].min())
after = df['f1'].var()
print(round(before-after, 2))