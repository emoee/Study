# 고객과 잘 맞는 타입 추천 :)

# basic1 데이터와 basic3 데이터를 'f4'값을 기준으로 병합하고,
# 병합한 데이터에서 r2결측치를 제거한다음, 앞에서 부터 20개 데이터를 선택하고 
# 'f2'컬럼 합을 구하시오

# basic1.csv: 고객 데이터
# basic3.csv: 잘 어울리는 관계 데이터 (추천1:r1, 추천2:r2)

import pandas as pd
b1 = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
b3 = pd.read_csv("../input/bigdatacertificationkr/basic3.csv")

df = b1.merge(b3, how='inner', on='f4')
df = df.dropna(subset=['r2'])
result = df['f2'].head(20).sum()
print(result)


# 고객과 잘 맞는 타입 추천 :)
# basic1 데이터와 basic3 데이터를 'f4'값을 기준으로 병합하고,
# 병합한 데이터에서 r2결측치를 제거한다음, 앞에서 부터 20개 데이터를 선택하고 'f2'컬럼 합을 구하시오

# basic1.csv: 고객 데이터
# basic3.csv: 잘 어울리는 관계 데이터 (추천1:r1, 추천2:r2)

import pandas as pd
b1 = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
b2 = pd.read_csv("../input/bigdatacertificationkr/basic3.csv")

df = pd.merge(left = b1, right = b2, how = 'left', on = 'f4')

df = df.dropna(subset=['r2'])
df = df.reset_index()
df = df[:20]
print(df['f2'].sum())