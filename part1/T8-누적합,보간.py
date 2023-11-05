'''
주어진 데이터 셋에서 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산한다. 이때 발생하는 누적합 결측치는 바로 뒤의 값을 채우고, 누적합의 평균값을 출력한다. (단, 결측치 바로 뒤의 값이 없으면 다음에 나오는 값을 채워넣는다)

데이터셋 : basic1.csv
'''
# 라이브러리 및 데이터 불러오기
import numpy as np
import pandas as pd

df = pd.read_csv('/kaggle/input/bigdatacertificationkr/basic1.csv')

# 조건에 따른 누적합
df2 = df[df['f2']==1]['f1'].cumsum() # cumsum 누적합
df2
'''
1       70.0
2      131.0
6      191.0
7      292.0
9      366.0
13     416.0
14     483.0
16       NaN
19     534.0
20       NaN
21     606.0
22     681.0
25     738.0
27     772.0
33       NaN
35     849.0
37       NaN
46     924.0
49    1002.0
51    1084.0
53       NaN
55       NaN
58       NaN
62    1170.0
65       NaN
66    1222.0
69    1318.0
72       NaN
77    1414.0
80    1464.0
82    1514.0
86       NaN
88    1580.0
91    1658.0
93       NaN
94    1701.0
95    1754.0
Name: f1, dtype: float64
'''

# 결측치 처리 (뒤에 나오는 값으로 채움)
df2 = df2.fillna(method = 'bfill') 
# method : 결측값을 변경할 방식입니다. bfill로 할경우 결측값을 바로 아래 값과 동일하게 변경합니다.
'''
df.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
value : 결측값을 대체할 값입니다. dict형태로도 가능합니다.
method : 결측값을 변경할 방식입니다. bfill로 할경우 결측값을 바로 아래 값과 동일하게 변경합니다.
ffill로 할 경우 결측값을 바로 위 값과 동일하게 변경합니다.
axis : {0 : index / 1 : columns} fillna 메서드를 적용할 레이블입니다.
inplace : 원본을 변경할지 여부입니다. True일 경우 원본을 변경하게 됩니다.
limit : 결측값을 변경할 횟수입니다. 위에서부터 limit로 지정된 갯수만큼만 변경합니다.
downcast : 다운캐스트할지 여부입니다. downcast='infer'일 경우 float64를 int64로 변경합니다.
'''

# 평균 출력
print(df2.mean())

# 정답 : 980.3783783783783