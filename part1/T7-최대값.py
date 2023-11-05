'''
'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오!

데이터셋 : basic1.csv
오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
'''
# 라이브러리 및 데이터 불러오기
import numpy as np
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
df.head(5)

# ESFJ 값을 가진 데이터 확인
df[df['f4'] == 'ESFJ']

# 값 변경하기
df['f4'] = df['f4'].replace('ESFJ', 'ISFJ')
df[df['f4'] == 'ESFJ']

# 2개의 조건에 맞는 값중 age컬럼의 최대값,'age'컬럼의 최대값을 출력
con1 = df['city'] == '경기'
con2 = df['f4'] == 'ISFJ'

df[con1 & con2]['age'].max()
# 정답 : 90.0