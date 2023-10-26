from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/seoul_bicycle.csv')
print(df.info())
'''
Data columns (total 11 columns):
 #   Column  Non-Null Count   Dtype  
---  ------  --------------   -----  
 0   대여일자    327231 non-null  object 
 1   대여소번호   327231 non-null  int64  
 2   대여소명    327231 non-null  object 
 3   대여구분코드  327231 non-null  object 
 4   성별      272841 non-null  object 
 5   연령대코드   327231 non-null  object 
 6   이용건수    327231 non-null  int64  
 7   운동량     327231 non-null  object 
 8   탄소량     327231 non-null  object 
 9   이동거리    327231 non-null  float64
 10  이용시간    327231 non-null  int64  
dtypes: float64(1), int64(3), object(7)
memory usage: 27.5+ MB
'''

df['대여일자'] =pd.to_datetime(df['대여일자']) #object를 datetime으로 변환해서 대입
#print(df.info())
# 0   대여일자    327231 non-null  datetime64[ns]
#print(df['대여일자'].dt.year)

bins = [0, 6000, 100000, df['이동거리'].max()] #구간 범위 설정
labels = ['적음', '보통', '많음'] #레이블은 구간 범위보다 1 적어야함
print(pd.cut(df['이동거리'], bins, labels=labels, right=False)) #right가 false면 우측 범위 포함하지 않음

df['이동거리_cut'] = pd.cut(df['이동거리'], bins=3) #bins 구간의 갯수
print(df['이동거리_cut'].value_counts())
'''
(-56709.053, 18903017.647]      327216
(18903017.647, 37806035.293]        12
(37806035.293, 56709052.94]          3
Name: 이동거리_cut, dtype: int64
'''
#첫번째 구간에 데이터가 쏠려 다른 방법 사용하는 것이 좋을 것
#아래의 방법은 데이터 분포를 최대한 비슷하게 유지해 구간을 분할
df['이동거리_qcut'] = pd.qcut(df['이동거리'], q=3) #bins 구간의 갯수
print(df['이동거리_qcut'].value_counts())
'''
(-0.001, 9030.0]          109095
(60470.0, 56709052.94]    109072
(9030.0, 60470.0]         109064
Name: 이동거리_qcut, dtype: int64
'''
#위의 방법은 균일하지만 간격이 일정하지 않음. 간격을 일정하게 나눠 균등분할
qcut_bins = [0, 0.2, 0.8, 1]
qcut_labels = ['적음', '보통', '많음'] #레이블은 범위보다 1개 작게 설정
print(pd.qcut(df['이동거리'], qcut_bins, labels=qcut_labels).value_counts())
'''
보통    196307
적음     65482
많음     65442
'''