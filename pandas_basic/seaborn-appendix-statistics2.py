from IPython.display import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

# Unicode warning 제거 (폰트 관련 경고메시지)
plt.rcParams['axes.unicode_minus']=False

# 그래프 출력 사이즈 설정
plt.rcParams["figure.figsize"] = (10, 8)

iris = sns.load_dataset('iris')
tips = sns.load_dataset("tips")

### pairplot
# 그리드 형태로 각 집합의 조합에 대해 히스토그램과 분포도 그림
# 숫자형만 가능
sns.set_style('white')
sns.pairplot(iris)
plt.show()

### relplot 
# 두 컬럼간 상관관계 비교 가능, 단 implot처럼 선형관계 따로 그리진 않음
sns.relplot(x="total_bill", y="tip", hue="day", height=5, data=tips)
plt.show()

sns.relplot(x="total_bill", y="tip", hue="day", col="time", height=5, data=tips) # col 옵션으로 그래프 분할 가능
plt.show()

sns.relplot(x="total_bill", y="tip", hue="day", row="sex", col="time", palette='CMRmap_r', height=5, data=tips) # row, col 두 옵션으로 분할
plt.show()

x = np.random.randn(100)
### rugplot
# rug는 데이터 위치를 x축 위에 작은 선분(rug)으로 나타내 데이터의 위치 및 분포 보여줌
sns.kdeplot(x=x)
sns.rugplot(x=x)
plt.show()

### swarmplot
sns.swarmplot(x='day', y='total_bill', data=tips, color='.25')
plt.show()

sns.boxplot(x='day', y='total_bill', data=tips) # 박스플롯 위에 그리기
sns.swarmplot(x='day', y='total_bill', data=tips, color='.25')
plt.show()

### violinplot
# 바이올린처럼 생김, 컬럼에 대한 데이터의 비교 분포도 확인 가능
# 곡선진 부분(뚱뚱한 부분)이 데이터의 분포 / 양쪽 끝(뾰족한 부분)은 데이터 최소.최대값
sns.violinplot(x=tips["total_bill"]) # (-) 바이올린 기본
plt.show()
sns.violinplot(y="day", x="total_bill", data=tips) # (|)가로로 뉘인 바이올린
plt.show()

# hue 옵션을 사용 안하면 바이올린이 대칭이어 비교 분포의 큰 의미 x, 근데 옵션을 주면 단일 컬럼에 대한 바이올린 모양의 비교 가능
sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted")
plt.show()

# split으로 합쳐서 보기 가능
sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted", split=True)
plt.show()

### implot
# 컬럼간의 선형관계 확인하기 용이한 차트. outlier 짐작 가능
sns.lmplot(x="total_bill", y="tip", height=5, data=tips)
plt.show()

# hue 옵션으로 다중 선형관계 그리기 가능
sns.lmplot(x="total_bill", y="tip", hue="smoker", height=5, data=tips)
plt.show()

# col 옵션으로 그래프 별도로 그리기 가능. col_wrap으로 한줄에 표기할 컬럼 갯수
sns.lmplot(x='total_bill', y='tip', hue='smoker', col='day', col_wrap=2, height=5, data=tips)
plt.show()
