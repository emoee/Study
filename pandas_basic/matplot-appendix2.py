from IPython.display import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# Unicode warning 제거 (폰트 관련 경고메시지)
plt.rcParams['axes.unicode_minus']=False

# 그래프 출력 사이즈 설정
plt.rcParams["figure.figsize"] = (10, 8)

'''
# scatter
x = np.random.rand(50)
y = np.random.rand(50) # 랜덤값
colors = np.arange(50) # 순차
area = x * y * 250

#plt.scatter(x, y, s = area, c = colors)
#plt.show()

plt.figure(figsize=(12, 6))

## 투명도 지정 0에 가까울 수록 투명
plt.subplot(131)
plt.scatter(x, y, s=area, color='purple', alpha=0.1)
plt.title('alpha=0.1')

plt.subplot(132)
plt.title('alpha=0.5')
plt.scatter(x, y, s=area, color='purple', alpha=0.5)

plt.subplot(133)
plt.title('alpha=1.0')
plt.scatter(x, y, s=area, color='purple', alpha=1.0)

plt.show()
'''

'''
# bar = 세로, barh = 가로 그래프
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

plt.figure(figsize=(6, 3))
# plt.bar(x, y)
plt.bar(x, y, align='center', alpha=0.7, color='red')
plt.xticks(x) # plt.yticks(x) 축 변환
plt.ylabel('Number of Students')
plt.title('Subjects')

plt.show()

x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]

# 넓이 지정
width = 0.35

# subplots 생성
fig, axes = plt.subplots()

# 넓이 설정
axes.barh(x - width/2, y_1, width, align='center', alpha=0.5) #bar 세로 그래프
axes.barh(x + width/2, y_2, width, align='center', alpha=0.8)

# xtick 설정
plt.yticks(x)
axes.set_yticklabels(x_label)
plt.xlabel('Number of Students')
plt.title('Subjects')

plt.legend(['john', 'peter'])

plt.show()
'''

''''''
# line plot
x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x)

plt.plot(x, y)

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin graph', fontsize=18)

plt.grid()

plt.show()

