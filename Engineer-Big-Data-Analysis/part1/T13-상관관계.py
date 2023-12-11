# %% [code]
# 상관관계 구하기
# 주어진 데이터에서 상관관계를 구하고, 
# quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 출력

# - 데이터셋 : ../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - 스크립트 방식 권장: File -> Editor Type -> Script

import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv("../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv")
#print(df.head())

df_corr = df.corr()
df_corr = df_corr['quality']
df_corr = df_corr.drop(index = 'quality')
corr_max = abs(df_corr).max()
corr_min = abs(df_corr).min()
result = round((corr_max + corr_min), 2)
print(result)