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

'''
# line plot
x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x)

plt.plot(x, y)

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin graph', fontsize=18)

plt.grid()

plt.show()
'''

'''
# areaplot
areax = np.arange(1, 21)
areay = np.random.randint(low=5, high=10, size=20)
plt.fill_between(areax, areay, color="green", alpha=0.5)
plt.plot(areax, areay, color="green", alpha=0.8) # 경계선 굵게 
plt.show()

x = np.arange(1, 10, 0.05)
y_1 =  np.cos(x)+1
y_2 =  np.sin(x)+1
y_3 = y_1 * y_2 / np.pi

plt.fill_between(x, y_1, color="green", alpha=0.1)
plt.fill_between(x, y_2, color="blue", alpha=0.2)
plt.fill_between(x, y_3, color="red", alpha=0.3) # 그래프 겹쳐서 표현 가능
plt.show()
'''

'''
# histogram
N = 100000
bins = 30

x = np.random.randn(N)

fig, axs = plt.subplots(1, 3, 
                        sharey=True, 
                        tight_layout=True
                       )

fig.set_size_inches(12, 5)

axs[0].hist(x, bins=bins)
axs[1].hist(x, bins=bins*2) # bin의 크기 변화 : 히스토그램의 가로축 구간의 개수를 지정
axs[2].hist(x, bins=bins*4)

plt.show()

N = 100000
bins = 30

x = np.random.randn(N)

fig, axs = plt.subplots(1, 2, 
                        tight_layout=True
                       )
fig.set_size_inches(9, 3)

# density=True 값을 통하여 Y축에 density (밀도)를 표기할 수 있습니다.
axs[0].hist(x, bins=bins, density=True, cumulative=True) # cumulative = True => 누적 히스토그램
axs[1].hist(x, bins=bins, density=True)

plt.show()
'''

'''
# pie chart
labels = ['Samsung', 'Huawei', 'Apple', 'Xiaomi', 'Oppo', 'Etc']
sizes = [20.4, 15.8, 10.5, 9, 7.6, 36.7]
explode = (0.3, 0, 0, 0, 0, 0) # 파이에서 튀어나온 비율

# texts, autotexts  텍스트 효과
patches, texts, autotexts = plt.pie(sizes, 
                                    explode=explode, 
                                    labels=labels,  
                                    autopct='%1.1f%%',
                                    shadow=True, 
                                    startangle=90)

plt.title('Smartphone pie', fontsize=15)

for t in texts:
    t.set_fontsize(12)
    t.set_color('gray')

# pie 위의 텍스트에 대한 스타일 적용
for t in autotexts:
    t.set_color("white")
    t.set_fontsize(18)

plt.show()
'''

# box plot
# 샘플 데이터 생성
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))

outlier_marker = dict(markerfacecolor='r', marker='D') # 다이아 모양에 빨간색

plt.tight_layout()
plt.title('Horizontal Box Plot', fontsize=15)
plt.boxplot(data, vert=False,  flierprops=outlier_marker) # vert=False 축 변경, flierprops 마커 심볼 변경

plt.show()

