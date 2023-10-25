import pandas as pd
import numpy as np


'''Series 기본 동작 방법'''
arr = np.arange(100,105)
#print(arr)

s = pd.Series(arr) #series 1차원 배열
#print(s)

s = pd.Series(arr, dtype='int32')
#print(s)

s = pd.Series(['부장', 2.5, 5, '사원']) #다양한 데이터 타입 일 시 object 타입
#print(s)
s.index #0부터 순차적 부여
s.index = list('abcd') #인덱스 지정 가능
#print(s[2]) #3번 째 데이터
#print(s['c'])

np.random.seed(0)
s = pd.Series(np.random.randint(10000, 20000, size=(10,)))
#print(s > 15000) #참 거짓 값 

s.values #값만 출력가능
#print(s.ndim) #1차원이기 때문에 1

s.shape #데이터 갯수

t = pd.Series(['선화', '강호', np.nan, '소정', '우영']) #np.nan = 결측치 데이터. 비어있는 값 대입할 때
t.isnull()
t.isna()
t.notnull()

#print(s[1:3])

'''연습'''
A = pd.Series([3.0, 5.0, 7.0, 9.0, 11.0], dtype='float32')
#print(A)

sample = pd.Series([10,20,30,40,50])
sample.index = list('가나다라마')
#print(sample['나':'라'])

np.random.seed(20)
sample2 = pd.Series(np.random.randint(100, 200, size=(15,)))
#print(sample2[sample2 <= 160])

'''DataFrame 기본 동작 방법'''
df = pd.DataFrame([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]], columns=['가', '나', '다'])

df.rename(columns={'가': '바'},inplace=True) #컬럼명 변경 가능 inplace 옵션으로 변경사항 바로 적용가능

data = { #딕셔너리로 생성 가능, key 값이 자동으로 column 명으로 지정
    'name': ['Kim', 'Lee', 'Park'], 
    'age': [24, 27, 34], 
    'children': [2, 1, 3]
}
df = pd.DataFrame(data)

#시리즈와 대부분 비슷

'''연습 문제'''
data = {
    'food' : ['KFC', 'McDonald', 'SchoolFood'],
    'price' : [1000, 2000, 2500],
    'rating' : [4.5, 3.9, 4.2]
}
df = pd.DataFrame(data)

print(df[['food','rating']])
df.rename(columns={'food':'place'},inplace=True)
print(df)
