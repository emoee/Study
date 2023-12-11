# 베르누이 분포와 이항분포**

# [베르누이 분포] 다음 데이터는 100번의 시도에서 각각 성공(1) 또는 실패(0)를 나타냅니다. 
# 이 데이터를 바탕으로 각 시도의 성공 확률을 계산하시오. 
# [이항분포] 1번 문제에서 계산한 성공 확률을 사용하여, 
# 100번의 시도 중 정확히 60번 성공할 확률을 계산하시오.

import pandas as pd
from scipy import stats

df = pd.read_csv("/kaggle/input/bigdatacertificationkr/t3_success.csv")
total = len(df)
n = 100
t = 60
success = df['Success'].sum()
result = success/total
result2 = stats.binom.pmf(t, n, result)
# binom.pmf(k, n, p) 함수는 이항 분포의 확률 질량 함수(Probability Mass Function, PMF)를 계산하는 데 사용됩니다. 

print(result, result2)