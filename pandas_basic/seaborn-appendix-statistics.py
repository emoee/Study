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

titanic = sns.load_dataset('titanic')
tips = sns.load_dataset("tips")
'''
### catplot
# 검은색 bar는 오차막대(error bar), 신뢰구간(confidence interval) 95%
sns.catplot(x = 'who', y = 'survived', col= 'pclass',
            row= 'embarked', kind='bar', height=2.5, data= titanic)
plt.show()

sns.catplot(x = 'survived', col= 'pclass',
            row= 'embarked', kind='count', height=2.5, data= titanic)
plt.show()

sns.catplot(x = 'who', y = 'age', col= 'pclass',
            row= 'embarked', kind='box', height=2.5, data= titanic)
plt.show()

sns.catplot(x = 'who', y = 'fare', col= 'pclass',
            row= 'embarked', kind='violin', height=2.5, data= titanic)
plt.show()

### countplot
# 해당 column을 구성하고 있는 value들을 구분하여 보여줌
sns.set(style='darkgrid')
sns.countplot(x="class", hue="who", data=titanic) # 세로
plt.show()

sns.countplot(y="class", hue="who", data=titanic) # 가로
plt.show()

sns.countplot(x="class", hue="who", palette='copper', data=titanic) # 색상 팔레트
plt.show()

### heatmap
uniform_data = np.random.rand(10, 12)
plt.figure(figsize=(10, 8))
sns.heatmap(uniform_data, annot=True, )
plt.show()

titanic.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(titanic.corr(), annot=True, cmap="YlGnBu")
plt.show()
'''
### histplot 
# matplotlib의 hist + kdeplot 통합한 그래프
# 분포와 밀도를 확인 가능
# 샘플데이터 생성

x = np.random.randn(100)
sns.histplot(x=x)
plt.show()

x = pd.Series(x, name="x variable")
sns.histplot(x=x,  color="y")
# 구버전
# sns.distplot(x)
plt.show()

sns.histplot(y=x)
# 구버전
# sns.distplot(x, vertical=True)
plt.show()

### jointplot
# scatter(산점도) + histogram(분포) 동시에 그리기 가능
# 숫자형 데이터만 표현 가능
sns.jointplot(x="total_bill", y="tip", height=7, data=tips)
plt.show()

sns.jointplot(x="total_bill", y="tip", height=7, data=tips, kind="reg") #  kind='reg' =>선형관계 표현하는 regression 라인 
plt.show()

sns.jointplot(x="total_bill", y="tip", height=7, data=tips, kind="hex") # kind='hex' => hex 모양의 밀도를 확인 가능 / 벌집모양
plt.show()

iris = sns.load_dataset('iris')
sns.jointplot(x="sepal_width", y="petal_length", height=7, data=iris, kind="kde", color="g") # kind='kde' => 등고선 모양으로 밀집도 확인 가능(부드러운 선)
plt.show()

### kdeplot
# histogram보다 부드러운 형태의 분포 곡선
sns.kdeplot(x=x)
plt.show()