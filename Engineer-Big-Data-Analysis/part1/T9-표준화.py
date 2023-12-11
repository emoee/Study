'''
수치형 변수 변환하기

주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오

데이터셋 : basic1.csv
오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
'''
import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')

scaler = StandardScaler()
df['f5'] = scaler.fit_transform(df[['f5']])

result = df['f5'].median()
print(result)

# 라이브러리 및 데이터 불러오기
import numpy as np
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
df.head(5)
'''
	id	age	city	f1	f2	f3	f4	f5
0	id01	2.0	서울	NaN	0	NaN	ENFJ	91.297791
1	id02	9.0	서울	70.0	1	NaN	ENFJ	60.339826
2	id03	27.0	서울	61.0	1	NaN	ISTJ	17.252986
3	id04	75.0	서울	NaN	2	NaN	INFP	52.667078
4	id05	24.0	서울	85.0	2	NaN	ISFJ	29.269869
'''

# 표준화
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['f5'] = scaler.fit_transform(df[['f5']])
df.head(5)
'''
	id	age	city	f1	f2	f3	f4	f5
0	id01	2.0	서울	NaN	0	NaN	ENFJ	1.220815
1	id02	9.0	서울	70.0	1	NaN	ENFJ	0.127343
2	id03	27.0	서울	61.0	1	NaN	ISTJ	-1.394535
3	id04	75.0	서울	NaN	2	NaN	INFP	-0.143667
4	id05	24.0	서울	85.0	2	NaN	ISFJ	-0.970085
'''

# 중앙값 출력
print(df['f5'].median())
# 정답 : 0.260619629559015