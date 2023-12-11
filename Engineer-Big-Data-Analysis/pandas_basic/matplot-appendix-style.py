import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.family'] = "AppleGothic"
plt.rcParams["figure.figsize"] = (10, 8)


plt.plot(np.arange(10), np.arange(10)*2, marker='o', linestyle='', markersize= 5, color='b', alpha=0.1)
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='o', linestyle='-', markersize= 10, color='c', alpha=0.3)
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='v', linestyle='--', markersize= 15, color='y', alpha=0.5)
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='+', linestyle='-.', markersize= 20, color='r', alpha=0.7)
plt.plot(np.arange(10), np.arange(10)*2 - 40, marker='*', linestyle=':', markersize= 25, color='k', alpha=1.0)

# 타이틀 & font 설정
plt.title('마커 크기 & 선 종류 & 색상 & 투명도 지정', fontsize=15)

# X축 & Y축 Label 설정
plt.xlabel('X축', fontsize=10)
plt.ylabel('Y축', fontsize=10)

# X tick, Y tick 설정
plt.xticks(rotation=90)
plt.yticks(rotation=30)

plt.grid() #그리드 옵션 칸이 나눠짐

# annotate 설정 그래프 주석
plt.annotate('코로나 사태 발생 지점', xy=(3, -20), xytext=(3, -25), arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
