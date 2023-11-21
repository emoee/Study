# 이상치를 찾아라
# 데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오

# 강의 영상 : https://youtu.be/ipBW5D_UJEo
# 데이터셋 : titanic
# 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# 데이터 위치 "../input/titanic/train.csv" (copy&edit가 아닐 경우 별도로 데이터셋 불러와야 함)

import pandas as pd
import numpy as np
df = pd.read_csv('../input/titanic/train.csv')
Q1 = np.percentile(df['Fare'], 25)
Q3 = np.percentile(df['Fare'], 75)

IQR = Q3 - Q1

out1 = df[df['Fare'] < (Q1 - 1.5 * IQR)]
out3 = df[df['Fare'] > (Q3 + 1.5 * IQR)]

print(sum(out1['Sex'] == 'female') + sum(out3['Sex'] == 'female'))

# IQR 구하기
# pandas 활용
# Q1 = df[col].quantile(.25)
# Q3 = df[col].quantile(.75)

# numpy 활용
# Q1 = np.percentile(df[col], 25)
# Q3 = np.percentile(df[col], 75)

# IQR = Q3 - Q1
# Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np
#df = pd.read_csv('../input/titanic/train.csv')

import seaborn as sns
df = sns.load_dataset("titanic")
# 간단한 탐색적 데이터 분석 (EDA)
print(df.head(5))
print(df.info())

# IQR 구하기
Q1 = np.percentile(df['fare'], 25)
Q3 = np.percentile(df['fare'], 75)
IQR = Q3 - Q1
print(IQR)

# 이상치 데이터 구하기
left = Q1 - (1.5 * IQR)
right = Q3 + (1.5 * IQR)
print(left, right)

data1 = df[df['fare'] < left] # 조건보다 작은 값
data2 = df[df['fare'] > right] # 조건보다 큰 값
print(len(data1), len(data2))

# 이상치 데이터에서 여성 수 구하기, 출력하기 print()
print(len(data2[data2['sex'] == 'female']))
print(sum(data2['sex'] == 'female'))
# 정답  : 70
