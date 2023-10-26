from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df = sns.load_dataset('titanic')

#groupby는 aggregate하는 통계함수와 같이 적용함
print(df.groupby('sex').mean())
# 성별, 좌석등급 별 통계
print(df.groupby(['sex', 'pclass'])['survived'].mean())
# DataFrame으로 출력 ()
#print(pd.DataFrame(df.groupby(['sex', 'pclass'])['survived'].mean()))
# index 초기화
print(df.groupby(['sex', 'pclass'])['survived'].mean().reset_index())

#여러개의 통계값 적용시 agg() 사용
# 성별, 좌석등급 별 통계, 평균값, 합계
print(df.groupby(['sex', 'pclass'])[['survived', 'age']].agg(['mean', 'sum']))

'''연습 문제'''
def changeClass(x):
    if x == 'First':
        return '일등석'
    elif x == 'Second':
        return '이등석'
    elif x == 'Third':
        return '삼등석'
    
df['class'].apply(changeClass) #apply 함수 적용
print(df['class'].apply(changeClass).head(3))
print(df.head(3))

print(df.groupby(['pclass'])['survived'].mean())
print(df.groupby(['embarked'])['survived'].aggregate(['mean', 'var']))
print(df.groupby(['who', 'pclass'])['survived'].aggregate(['mean', 'sum']))

print("===")
print(df.groupby('sex')['age'].mean()) 
#람다식
#df['age'] = df.groupby('sex')['age'].apply(lambda x : x.fillna(x.mean())) 

#풀어서
age_group_means = df.groupby('sex')['age'].transform('mean')
df['age'] = df['age'].fillna(age_group_means)

# 검증코드
print(df['age'].isnull().sum())
print(f"age 평균: {df['age'].mean():.2f}")