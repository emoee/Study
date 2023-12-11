import matplotlib.pyplot as plt
import pandas as pd
from mySUNI import cds
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# Unicode warning 제거 (폰트 관련 경고메시지)
plt.rcParams['axes.unicode_minus']=False

# 한글 폰트 설정
plt.rc('font', family = 'AppleGothic') # MacOs

# 그래프 출력 사이즈 설정
plt.rcParams["figure.figsize"] = (10, 8)

df = pd.read_csv('https://bit.ly/2Vk0zLr')
print(df.head(5))

'''line'''
#df['분양가'].plot(kind='line')
#plt.show()

df_seoul = df.loc[df['지역'] == '서울']
print(df_seoul)
df_seoul_year = df_seoul.groupby('연도').mean()
print(df_seoul_year)

#df_seoul_year['분양가'].plot(kind='line')
#plt.show()

'''bar'''
print(df.groupby('지역')['분양가'].mean())
#df.groupby('지역')['분양가'].mean().plot(kind='bar') #세로
#df.groupby('지역')['분양가'].mean().plot(kind='barh') #가로

#plt.show()

'''hist'''
df['분양가'].plot(kind='hist')
plt.show()

'''커널 밀도 그래프 : 히스토그램과 유사 부드러운 라인'''
df['분양가'].plot(kind='kde')
plt.show()

'''hexbin: 고밀도 산점도 그래프, x, y 값 모두 numeric. 데이터의 밀도 추정.'''
df.plot(kind='hexbin', x='분양가', y='연도', gridsize = 20) # 벌집 모양
plt.show()

'''box plot'''
df_seoul['분양가'].plot(kind='box')
plt.show()

from IPython.display import Image
# image source : https://justinsighting.com/how-to-interpret-box-plots/
#Image('https://justinsighting.com/wp-content/uploads/2016/12/boxplot-description.png')
#IQR은 Inter Quantile Range의 약어로써, (3Q - 1Q) * 1.5 값입니다.

'''pie''' 
df.groupby('연도')['분양가'].count().plot(kind='pie')
plt.show()

'''scatter plot : 점으로 데이터 표기, 데이터 분포도, numeric.'''
df.plot(x='월', y='분양가', kind='scatter')
plt.show()