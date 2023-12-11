# %% [code]
# city와 f4를 기준으로 f5의 평균값을 구한 다음, 
# f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
# - 데이터셋 : basic1.csv 

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

df = df.groupby(['city', 'f4'])
df = df['f5'].mean()
#print(df)
df = df.reset_index().sort_values('f5', ascending = False)
result = round(df['f5'].head(7).sum(),2)
print(result)

# %% [code]
# city와 f4를 기준으로 f5의 평균값을 구한 다음, 
# f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
# - 데이터셋 : basic1.csv 

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df = df.groupby(['city', 'f4'])[['f5']].mean() ## WHY???? []????

df = df.reset_index().sort_values('f5', ascending=False).head(7) # dataframe 전환 후 상위 7개 출력
print(round(df['f5'].sum(), 2))

# #결과값 : 643.68