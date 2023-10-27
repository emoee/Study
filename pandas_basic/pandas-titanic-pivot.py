from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

def transform_who(x):
    if x == 'man':
        return '남자'
    elif x == 'woman':
        return '여자'
    else:
        return '아이'
    
df['who'].apply(transform_who) #apply 함수 적용
print(df['who'].apply(transform_who).value_counts())

def transform_who(x):
    return x['fare'] / x['age']

df.apply(transform_who, axis=1)
df['survived'].apply(lambda x: '생존' if x == 1 else '사망') #람다식 사용 가능
print(df['survived'].apply(lambda x: '생존' if x == 1 else '사망').value_counts())


print(df.pivot_table(index='who', values='survived'))
# columns에 그룹을 표기
print(df.pivot_table(columns='who', values='survived'))

# 인덱스는 행에 표시 컬럼은 열에 표시
print(df.pivot_table(index='who', columns='pclass', values='survived'))

#통계 함수 적용 가능
df.pivot_table(index='who', columns='pclass', values='survived', aggfunc=['sum', 'mean'])