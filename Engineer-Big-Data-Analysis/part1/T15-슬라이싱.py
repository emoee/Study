# %% [code]
# %% [code]
# 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음 
# f1의 결측치를 중앙값으로 채운다.
# 그리고 f4가 ISFJ와 f5가 20 이상인 
# f1의 평균값을 출력하시오!

# - 데이터셋 : basic1.csv 

import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df = df.sort_values('age', ascending = False).head(20)
df['f1'] = df['f1'].fillna(df['f1'].median())
con = (df['f4'] == 'ISFJ') & (df['f5'] >= 20)
result = df[con]['f1'].mean()
print(result)

# %% [code]
# 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음 
# f1의 결측치를 중앙값으로 채운다.
# 그리고 f4가 ISFJ와 f5가 20 이상인 
# f1의 평균값을 출력하시오!

# - 데이터셋 : basic1.csv 

import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df = df.sort_values('age', ascending = False).head(20)
#print(df)

mid = df['f1'].median()
df['f1'] = df['f1'].fillna(mid)

con1 = (df['f4'] == 'ISFJ')
con2 = (df['f5'] >= 20)

print(df[(con1 & con2)]['f1'].mean())
# # 정답 : 73.875