from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
''' 
print(df.keys())
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'], dtype='object')
생존여부,좌석등급, 성별, 나이, 형제 + 배우자 수, 부모 + 자녀수, 좌석 요금, 탑승 항구, 좌석 등급, 남자.여자.아이, 성인 남자 여부, 데크 번호, 탑승항구 이름, 생존여부, 혼자 탑승 여부
'''
df_copy = df.copy() #데이터 프레임 복제
df_copy.loc[0,'age'] = 99999

#print(df.isnull().sum()) #결측치의 갯수 확인 isnull == isna
#print(df.isnull().sum().sum()) #전체 합산
#print(df.notnull().sum()) #결측치아닌 갯수

#print(df.loc[df['age'].isnull()]) #age값에 결측 데이터가 있는것 확인

#print(df_copy['age'].fillna(700).tail()) #결측치 700 변경
#print(df_copy['age'].fillna(df_copy['age'].mean()).tail) #결측치 평균값으로 채우기
#df_copy['age'].fillna(df_copy['age'].median()).tail() #중앙값으로 채우기

#df_copy['deck'].mode()[0] #최빈값(mode)으로 채울 때에는 반드시 0번째 index 지정하여 값을 추출한 후 채우기
#print(df_copy['deck'].fillna(df_copy['deck'].mode()[0]).tail())

'''
NaN 값이 있는 행 제거
기본 옵션 값은 how=any
any: 1개 라도 NaN값이 존재시 drop
all: 모두 NaN값이 존재시 drop
'''
#print(df_copy.dropna(how='any'))

'''연습 문제'''
#df.loc[df['age'].isnull(),'age'] = 30
#assert df['age'].isnull().sum() == 0
#assert df['age'].mean().round(4) == 29.7589

male = (df['sex'] == 'male')
female = (df['sex'] == 'female')
male_age = df.loc[male, 'age'].mean()
female_age = df.loc[female, 'age'].mean()

df.loc[male,'age'] = df.loc[male, 'age'].fillna(male_age)
df.loc[female,'age'] = df.loc[female, 'age'].fillna(female_age)
assert (df['age'].isnull().sum() == 0)
assert df['age'].mean().round(5) == 29.73603