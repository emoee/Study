# Q. 2022년 데이터 중 2022년 중앙값보다 큰 값의 데이터 수
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data2.csv", index_col='year')

con = (df.loc["2022년"].median())
result = sum(df.loc['2022년'] > con)
print(result)

# Q. 결측치 데이터(행)을 제거하고, 앞에서부터 60% 데이터만 활용해, 'f1' 컬럼 3사분위 값을 구하시오
# 60%가 소수점일 경우 절사(예: 36.6 일때 36으로 계산)
# data: t1-data1.csv
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
df = df.dropna().reset_index()

df2 = df[0:int(len(df)*0.6)]
result = df2['f1'].quantile(0.75)
print(result)

# Q. 결측치가 제일 큰 값의 컬럼명을 구하시오
import pandas as pd
df = pd.read_csv("../input/big-data-analytics-certification/t1-data1.csv")
result = df.isnull().sum()
print(result.index[3])