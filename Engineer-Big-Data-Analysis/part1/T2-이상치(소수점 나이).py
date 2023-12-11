# 이상치를 찾아라(소수점 나이)
# 주어진 데이터에서 이상치(소수점 나이)를 찾고 올림, 내림, 버림(절사)했을때 3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오

# 데이터셋 : basic1.csv
# 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# 강의 영상 : https://youtu.be/c3Fr9G-ZYdw

import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')

con = (df['age'] - np.floor(df['age'])) == 0 # 원래 값에서 버림한 것을 뺐을 때 0인 것
df = df[~con] # 소수점 나이 찾기

up = np.ceil(df['age']).mean()
down = np.floor(df['age']).mean()
drop = np.trunc(df['age']).mean()

print(up + down + drop)

# 라이브러리 및 데이터 불러오기
import numpy as np
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
print(df.head(5))
'''
     id   age city    f1  f2   f3    f4         f5
0  id01   2.0   서울   NaN   0  NaN  ENFJ  91.297791
1  id02   9.0   서울  70.0   1  NaN  ENFJ  60.339826
2  id03  27.0   서울  61.0   1  NaN  ISTJ  17.252986
3  id04  75.0   서울   NaN   2  NaN  INFP  52.667078
4  id05  24.0   서울  85.0   2  NaN  ISFJ  29.269869
'''

# 소수점 데이터 찾기
df = df[(df['age']-np.floor(df['age']))!= 0]
#np.floor() 함수는 주어진 숫자를 내림하여 정수로 반환하는 함수(소수점 이하를 버리고 정수 부분만 남김)
# 양수에서는 같지만 음수에서는 -5.5에서 내림을 하면 -6, 버림을하면 -5가 된다.

# 이상치를 포함한 데이터 올림, 내림, 버림의 평균값 
ageCeil = np.ceil(df['age']).mean()
ageFloor = np.floor(df['age']).mean()
ageTrunc = np.trunc(df['age']).mean()
print(ageCeil, ageFloor, ageTrunc)

# 평균값 더한 다음 출력
print(ageCeil + ageFloor + ageTrunc)