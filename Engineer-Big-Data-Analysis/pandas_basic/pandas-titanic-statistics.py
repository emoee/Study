from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
df = sns.load_dataset('titanic')
df.head()
#print(df.describe()) #요약통계
#print(df.describe(include='object')) #통계표
#print(df.count()) #개수
#print(df['age'].count())
#print(df.mean()) #평균
#print(df['age'].mean())

#print("성인 남성의 나이의 평균 구하기")
condition = (df['adult_male'] == True)
#print(df.loc[condition, 'age'].mean())

#skipna=False, NaN 값이 있는 column은 NaN 값으로 출력
#print(df.mean(skipna=False))
#print(df['age'].median()) #오름차순 중앙 값/ 짝수개면 중앙 값 2개의 평균 값 출력

#중앙값과 평균값은 다름
#print(f"나이 평균: {df['age'].mean():.5f}\n나이 중앙값: {df['age'].median()}\n차이: {df['age'].mean() - df['age'].median():.5f}")
#print("--")
#print(df.loc[:, ['age', 'fare']].sum())
#print(df['fare'].sum()) #합계

#print(df['age'].cumsum) #누적합
#print(df['age'].cumprod) #누적곱

# 평균
fare_mean = df['fare'].values.mean()

# 분산
my_var = ((df['fare'].values - fare_mean) ** 2).sum() / (df['fare'].count() - 1)
print(my_var)

#분산의  = 표준 편차
print(np.sqrt(df['fare'].var()))
print(df['fare'].std())

print(df['age'].agg(['min', 'max', 'count', 'mean']))

#분위
print(df['age'].quantile(0.1)) #분위 10% = 0.1 80% = 0.8

#고유값
print(df['who'].unique()) #개수 = nunique()

#최빈값 = 가장 많이 출현한 데이터
print(df['who'].mode())

#상관관계 컬럼별 상관관계 : -1~1, -1에 가까울 수록 반비례 관계, 1에 가까울수록 정비례 관계
print(df.corr())
df.corr()['survived']

'''연습 문제'''
condition1 = (df['fare'] >= 30) & (df['fare'] < 40)
condition2 = (df['pclass'] == 1)
print(df.loc[condition1 & condition2, 'age'].count())

print(df.loc[condition1 & condition2, 'age'].mean())