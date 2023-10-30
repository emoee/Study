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

