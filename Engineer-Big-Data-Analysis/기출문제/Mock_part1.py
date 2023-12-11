# 1. 첫번째 데이터 부터 순서대로 50:50으로 데이터를 나누고, 
# 앞에서 부터 50%의 데이터(이하, A그룹)는 'f1'컬럼의 결측치를 A그룹의 중앙값으로 채우고, 
# 뒤에서부터 50% 데이터(이하, B그룹)는 'f1'컬럼의 결측치를 B그룹의 최대값으로 채운 후, 
# A그룹과 B그룹의 표준편차 합을 구하시오

# 단, 소수점 첫째자리까지 구하시오 (둘째자리에서 반올림)

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

dfA = df[:int(len(df)/2)]
dfB = df[int(len(df)/2):]

dfA['f1'] = dfA['f1'].fillna(dfA['f1'].median())
dfB['f1'] = dfB['f1'].fillna(dfB['f1'].max())

dfA_Std = dfA['f1'].std()
dfB_Std = dfB['f1'].std()

result = round(dfA_Std + dfB_Std,2) 
print(result)

# 2. 'f4'컬럼을 기준 내림차순 정렬과 'f5'컬럼기준 오름차순 정렬을 순서대로 다중 조건 정렬하고나서 
# 앞에서부터 10개의 데이터 중 'f5'컬럼의 최소값 찾고, 
# 이 최소값으로 앞에서 부터 10개의 'f5'컬럼 데이터를 변경함. 
# 그리고 'f5'컬럼의 평균값을 계산함

# 단 소수점 둘째자리까지 출력(셋째자리에서 반올림)

import pandas as pd
df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

df = df.sort_values(['f4', 'f5'], ascending = [False, True])
f5min = df.head(10)['f5'].min()
df[:10]['f5'] = f5min

result = round(df['f5'].mean(),2)
print(result)

# 3. 'age' 컬럼의 IQR방식을 이용한 이상치 개수와 표준편차*1.5방식을 이용한 이상치의 개수를 더하시오

# IQR방식 : Q1 - 1.5 * IQR, Q3 + 1.5 * IQR에서 벗어나는 영역을 이상치라고 판단함 
# (Q1은 데이터의 25%, Q3는 데이터의 75% 지점임)
# 표준편차1.5방식: 평균으로부터 '표준편차1.5'를 벗어나는 영역을 이상치라고 판단함
import pandas as pd

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")

q1 = df['age'].quantile(0.25)
q3 = df['age'].quantile(0.75)
iqr = q3 - q1

b = q1 - 1.5 * iqr
a = q3 + 1.5 * iqr

result = sum((df['age'] > a) | (df['age'] < b))

std = df['age'].std() * 1.5
a = df['age'].mean()
result2 = sum((df['age'] > a+std) | (df['age'] < a-std))

result3 = result + result2
print(result3)