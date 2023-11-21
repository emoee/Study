# 주어진 데이터(basic2.csv)에서 주 단위 Sales의 합계를 구하고, 가장 큰 값을 가진 주와 작은 값을 가진 주의 차이를 구하시오(절대값)

# 데이터셋 : basic2.csv

import pandas as pd

df = pd.read_csv("../input/bigdatacertificationkr/basic2.csv", parse_dates=['Date'], index_col=0)

dfw = df.resample('W').sum() 
# df.resample('Q').min() = 분기 
# df.resample('B').sum() = 월~금
# df.resample('M').sum() = 월간
 
maxdf = dfw['Sales'].max()
mindf = dfw['Sales'].min()

print(maxdf-mindf)

# 정답 : 91639050