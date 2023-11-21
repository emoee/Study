'''
결측치 제거 및 그룹 합계에서 조건에 맞는 값 찾아 출력

주어진 데이터 중 basic1.csv에서 'f1'컬럼 결측 데이터를 제거하고, 'city'와 'f2'을 기준으로 묶어 합계를 구하고, 'city가 경기이면서 f2가 0'인 조건에 만족하는 f1 값을 구하시오
데이터셋 : basic1.csv
'''
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')

df = df[~df['f1'].isnull()]
df = df.reset_index()

df2 = df.groupby(['city', 'f2']).sum()

result = df2.iloc[0]['f1']
print(result)

# 라이브러리 및 데이터 불러오기
import numpy as np
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')
df.head(5)

# f1컬럼 결측치 제거
df = df[~df['f1'].isnull()]
df.head(5)

# 'city'와 'f2'을 기준으로 묶어 그룹 합계 계산
df2 = df.groupby(['city','f2']).sum()
print(df2)

# "city가 경기이면서 f2가 0'인 조건에 만족하는 f1 값"조건에 맞는 값 출력

print(df2.iloc[0]) # 데이터프레임에서 0번째 행 추출
print(df2.loc['경기','f1']) #  행:'경기'에 열:'f1'값 추출
print(df2['f1'][0])