from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

# concat()은 2개 이상의 DataFrame을 행 혹은 열 방향으로 연결
# merge()는 2개의 DataFrame을 특정 Key를 기준으로 병합할 때 활용

gas1 = pd.read_csv('data/gas_first_2019.csv', encoding='euc-kr')
gas2 = pd.read_csv('data/gas_second_2019.csv', encoding='euc-kr')
#print(gas1.shape)
#print(gas1.head(5))
#print(gas2.shape)
#print(gas2.head(5))

#print(pd.concat([gas1, gas2]).head(5))
#print(pd.concat([gas1, gas2]).iloc[90588:90593]) #데이터 행 개수가 차이가 나서 인덱스가 맞지 않음
gas = pd.concat([gas1, gas2], ignore_index=True)
print(gas.tail(5))

gas11 = gas1[['지역', '주소', '상호', '상표', '휘발유']]
gas22 = gas2[['상표', '번호', '지역', '상호', '주소', '경유', '휘발유']]
print(pd.concat([gas11, gas22], ignore_index=True)) #인덱스가 서로 맞지않아도 알아서 같은 컬럼끼리 병합 가능

gas1 = gas.iloc[:, :5]
gas2 = gas.iloc[:, 5:]
print(gas1.head(5))
print(pd.concat([gas1, gas2], axis=1)) #같은 인덱스 행끼리 연결

'''merge'''
df1 = pd.DataFrame({
    '고객명': ['박세리', '이대호', '손흥민', '김연아', '마이클조던'],
    '생년월일': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
    '성별': ['여자', '남자', '남자', '여자', '남자']})
df2 = pd.DataFrame({
    '고객명': ['김연아', '박세리', '손흥민', '이대호', '타이거우즈'],
    '연봉': ['2000원', '3000원', '1500원', '2500원', '3500원']})

print(pd.merge(df1, df2)) #default = inner
print(pd.merge(df1, df2, how = 'left')) #df1
print(pd.merge(df1, df2, how = 'right')) #df2
print(pd.merge(df1, df2, how = 'outer')) #both

#병합 할 컬럼의 이름이 다른 경우
df1 = pd.DataFrame({
    '이름': ['박세리', '이대호', '손흥민', '김연아', '마이클조던'],
    '생년월일': ['1980-01-02', '1982-02-22', '1993-06-12', '1988-10-16', '1970-03-03'],
    '성별': ['여자', '남자', '남자', '여자', '남자']})
df2 = pd.DataFrame({
    '고객명': ['김연아', '박세리', '손흥민', '이대호', '타이거우즈'],
    '연봉': ['2000원', '3000원', '1500원', '2500원', '3500원']})
print(pd.merge(df1, df2, left_on='이름', right_on='고객명')) #이렇게 하면 해당 컬럼이 삭제되지않음