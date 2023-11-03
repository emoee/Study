'''
결측치 처리

주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고, 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요!
데이터셋 : basic1.csv 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
강의 영상 : https://youtu.be/WqlpqBRn7x4
'''

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
# EDA - 결측값 확인(비율 확인)
df.isnull().sum() # 결측치가 몇개 있는지 확인
df.shape # 데이터 갯수 확인
df.isnull().sum()/df.shape[0] # 결측치 비율 확인
'''
id      0.00
age     0.00
city    0.00
f1      0.31
f2      0.00
f3      0.95
f4      0.00
f5      0.00
dtype: float64
'''

# 80%이상 결측치 컬럼, 삭제
df = df.drop(['f3'], axis=1)
df.shape
df['city'].unique()
# array(['서울', '부산', '대구', '경기'], dtype=object)

# 80%미만 결측치 컬럼, city별 중앙값으로 대체
seoul = df[df['city'] == '서울']['f1'].median()
busan = df[df['city'] == '부산']['f1'].median()
daegu = df[df['city'] == '대구']['f1'].median()
kyeonggi = df[df['city'] == '경기']['f1'].median()
print(seoul, busan, daegu, kyeonggi)
print(df['f1'].mean())

df['f1'] = df['f1'].fillna(df['city'].map({'서울':seoul,'경기':kyeonggi,'부산':busan,'대구':daegu}))

# f1 평균값 결과 출력
print(df['f1'].mean())

# 정답 : 65.52