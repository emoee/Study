from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
''' 
print(df.keys())
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'], dtype='object')
생존여부,좌석등급, 성별, 나이, 형제 + 배우자 수, 부모 + 자녀수, 좌석 요금, 탑승 항구, 좌석 등급, 남자.여자.아이, 성인 남자 여부, 데크 번호, 탑승항구 이름, 생존여부, 혼자 탑승 여부
'''

#생존자, 사망자 데이터 분석
#print(df.head(3))
#print(df.tail(3))
#df.info()
#df['who'].value_counts() #데이터 분포

#속성값 : ndim, shape, inex, columns, values, T
#ndim 차원 수 : 2, shape 데이터 갯수 : (891, 15), index, columns, values 모든 값 numpy array 형식, T 전치 : 열과 행 교환

#print(df.sort_index().head(5)) #오름차순 정렬 / 내림차순 : ascending=False
#print(df.sort_values(by='age').head()) #나이 기준으로 정렬
#print(df.sort_values(by=['fare', 'age'], ascending=[False, True]).head())

#print(df.loc[5, 'class'])

cond = (df['age'] >= 70)
df.loc[cond] #나이 조건에 맞는 데이터 추출

'''연습 문제'''

#print(df['embark_town'].value_counts())
#print(df['who'].value_counts())


con1 = (df['age'] >= 30)
con2 = (df['who'] == 'man')
#print(df.loc[con1 & con2].sort_values(by='fare',ascending=False).head(10))

con1 =(df['age'] >= 20) & (df['age'] < 40)
con2 = (df['pclass'] <= 2) 
print(df.loc[con1 & con2, ['survived', 'pclass', 'age', 'fare']].head(10))