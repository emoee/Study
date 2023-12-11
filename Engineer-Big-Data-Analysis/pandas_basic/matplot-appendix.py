import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# Unicode warning 제거 (폰트 관련 경고메시지)
plt.rcParams['axes.unicode_minus']=False

# 한글 폰트 설정
plt.rcParams['font.family'] = "AppleGothic"

# 그래프 출력 사이즈 설정
plt.rcParams["figure.figsize"] = (10, 8)

'''그래프'''
data = np.arange(1, 51)
plt.plot(data)
#plt.show()

data2 = np.arange(51, 101)

#plt.figure() #새로운 그래프 생성 이게 없으면 한 캔버스에 그려짐
plt.plot(data2)
#plt.show()


'''subplot 여러개의 plot 그리기
#subplot(row, column, index)
data3 = np.arange(100, 201)
plt.subplot(1, 3, 1) #plt.subplot(211) 콤마 없이 가능
plt.plot(data3)

data4 = np.arange(200, 301)
plt.subplot(1, 3, 2)
plt.plot(data4)

data5 = np.arange(300, 401)
plt.subplot(1, 3, 3)
plt.plot(data5)
#plt.show()
'''
'''subplots
#plt.subplots(행의 갯수, 열의 갯수)
fig, axes = plt.subplots(2, 3)

axes[0, 0].plot(data)
axes[0, 1].plot(data * data)
axes[0, 2].plot(data ** 3)
axes[1, 0].plot(data % 10)
axes[1, 1].plot(-data)
axes[1, 2].plot(data // 20)

plt.tight_layout()
'''

plt.title('타이틀 설정', fontsize=20) #타이틀
plt.xlabel('x축', fontsize=15) #축 이름
plt.ylabel('y축', fontsize=15) 

plt.xticks(rotation=90)
plt.yticks(rotation=30) #축 기울기

plt.legend(['x','y'], fontsize=15) #범례

plt.xlim(0, 20)
plt.ylim(50, 70) #한계 설정


plt.show()

from IPython.display import Image

# 출처: matplotlib.org
Image('https://matplotlib.org/_images/anatomy.png')