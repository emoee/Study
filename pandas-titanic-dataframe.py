from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import warnings

# warning 무시
warnings.filterwarnings('ignore')

# e notation 표현 방식 변경
pd.options.display.float_format = '{:.2f}'.format

# 모든 컬럼 표시
pd.set_option('display.max_columns', None)

df = sns.load_dataset('titanic')
''' 
print(df.keys())
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'], dtype='object')
생존여부,좌석등급, 성별, 나이, 형제 + 배우자 수, 부모 + 자녀수, 좌석 요금, 탑승 항구, 좌석 등급, 남자.여자.아이, 성인 남자 여부, 데크 번호, 탑승항구 이름, 생존여부, 혼자 탑승 여부
'''
df_copy = df.copy()
df_copy['VIP'] = True #새로운 데이터 컬럼 추가
df_copy.insert(5, 'RICH', df_copy['fare'] > 100) #컬럼 중간에 추가 좌석요금이 100이상이면 부자
#df_copy.drop(1) #행 삭제
df_copy.drop(np.arange(10)) #범위 지정 삭제 0~9행 삭제
df_copy.drop('class', axis=1).head() #열추가
#df_copy.drop('class', 1).head() #axis 생략 가능
#df_copy.drop(['who', 'deck', 'alive'], axis=1, inplace=True) #여러개 삭제 가능, inplace 옵션시 바로 적용 가능

df_copy2 = df.copy()
df_copy2['family'] = df_copy2['sibsp'] + df_copy2['parch']
df_copy2['gender'] = df_copy2['who'] + '-' + df_copy2['sex'] #문자열 추가 가능
df_copy2['round'] = round(df_copy2['fare'] / df_copy2['age'], 2) #소수점 자릿수 지정 2번째 자리까지

#print(df_copy2.loc[df_copy2['age'].isnull(), 'deck':].head()) #NaN 값이 있으면 결과는 NaN

##카테고리 타입으로 변경
#print(df_copy2['who'].astype('category').head(10))
df_copy2['who'] = df_copy2['who'].astype('category')

print(df_copy2['who'].cat.categories) #카테고리 타입의 속성 사용 가능 #출력
df_copy2['who'].cat.categories = ['아이', '남자', '여자'] #이름 변경
print(df_copy2['who'].value_counts())

'''연습 문제'''
