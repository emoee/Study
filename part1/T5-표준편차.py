'''
조건에 맞는 데이터 표준편차 구하기

주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오
데이터셋 : basic1.csv
오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
'''

import pandas as pd
import numpy as np

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')

conE = (df['f4'] == 'ENFJ') 
conI = (df['f4'] == 'INFP')

stdE = df[conE]['f1'].std() # 표준편차 : DataFrame.std()
stdI = df[conI]['f1'].std()

print(abs(stdE - stdI))

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
# 조건에 맞는 f1의 표준편차 (ENFJ, INFP)
enfj = df[df['f4']== 'ENFJ']['f1'].std()
infp = df[df['f4']== 'INFP']['f1'].std()
print(enfj, infp)

# 두 표준편차 차이 절대값 출력 
print(np.abs(enfj-infp))
# 정답 : 5.859621525876811