import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings


tips = sns.load_dataset("tips")

sns.catplot(x="sex", y="total_bill",
            hue="smoker", 
            data=tips, 
            kind="bar")
plt.show()

fig, axes = plt.subplots(1, 2)
fig.set_size_inches(12, 6)

axes[0].bar(tips['day'], tips['total_bill'])
axes[0].set_title('matplotlib')
sns.barplot(x="day", y="total_bill", data=tips, palette='Set1', ax=axes[1])
axes[1].set_title('seaborn')
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.arange(50)
area = x * y * 250 # 점의 크기

sns.scatterplot(x=x, y=y, size=area, sizes=(area.min(), area.max()), hue=area, palette='icefire')
plt.show()

## 한 캔버스에 3개 비교 131은 1열 3행 중 1행 133은 1열 3행 중  3행
## alpha가 0에 가까울수록 투명함
plt.figure(figsize=(20, 10))

plt.subplot(131)
g = sns.scatterplot(x=x, y=y, size=area, sizes=(area.min(), area.max()), color='green', alpha=0.1)
g.get_legend().remove()
plt.title('alpha=0.1')

plt.subplot(132)
plt.title('alpha=0.5')
g = sns.scatterplot(x=x, y=y, size=area, sizes=(area.min(), area.max()), color='green', alpha=0.5)
g.get_legend().remove()

plt.subplot(133)
plt.title('alpha=1.0')
g = sns.scatterplot(x=x, y=y, size=area, sizes=(area.min(), area.max()), color='green', alpha=0.9)
g.get_legend().remove()

plt.show()


# bar 그래프
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

sns.barplot(x=x, y=y, alpha=0.8, palette='YlGnBu')

plt.ylabel('Scores')
plt.title('Subjects')
plt.show()

# barh = 가로 그래프 / xticks => yticks 변경
x = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
y = [66, 80, 60, 50, 80, 10]

ax = sns.barplot(x=y, y=x, alpha=0.9, palette='YlOrRd')

plt.xlabel('Scores')
plt.title('Subjects')

plt.show()

# 비교 그래프 matplot 방법
x_label = ['Math', 'Programming', 'Data Science', 'Art', 'English', 'Physics']
x = np.arange(len(x_label))
y_1 = [66, 80, 60, 50, 80, 10]
y_2 = [55, 90, 40, 60, 70, 20]
width = 0.35

fig, axes = plt.subplots()
axes.bar(x - width/2, y_1, width, align='center', alpha=0.5)
axes.bar(x + width/2, y_2, width, align='center', alpha=0.8)

plt.xticks(x)
axes.set_xticklabels(x_label)
plt.ylabel('Number of Students')
plt.title('Scores')

plt.legend(['john', 'peter'])

plt.show()

# 비교 그래프 seaborn 방법
# 그래프를 임의로 그려야 하는 경우 -> matplotlib // DataFrame을 가지고 그리는 경우 -> seaborn
# hue 옵션으로 쉽게 그릴 수 있음
titanic = sns.load_dataset('titanic')

sns.barplot(x='sex', y='survived', hue='pclass', data=titanic, palette="muted")
plt.show()

# box plot
outlier_marker = dict(markerfacecolor='r', marker='o')
sns.boxplot(x='pclass', y='age', hue='survived', data=titanic, flierprops=outlier_marker)
plt.show()

# histogram
N = 100000
bins = 30

x = np.random.randn(N)

sns.histplot(x, bins=bins, kde=False, color='g') # kde = True => density가 y축에 표기됨
# 구 버전
# sns.distplot(x, bins=bins, kde=False, color='g')

plt.show()

# 분포표, 누적 분포표
N = 100000
bins = 30

x = np.random.randn(N)

fig, axes = plt.subplots(1, 2, tight_layout=True) # tight_layout: graph의 패딩을 자동으로 조절해주어 fit한 graph를 생성
fig.set_size_inches(12, 4)

sns.histplot(x=x, bins=bins, ax=axes[0])
sns.histplot(x=x, bins=bins, cumulative=True, ax=axes[1])

# 구버전
# sns.displot(x=x, bins=bins)
# sns.displot(x=x, bins=bins, cumulative=True)

plt.show()

# line plot
x = np.arange(0, 10, 0.1)
y = 1 + np.sin(x)

# grid 스타일을 설정할 수 있습니다. 
# whitegrid, darkgrid, white, dark, ticks
sns.set_style("darkgrid")

sns.lineplot(x=x, y=y)

plt.xlabel('x value', fontsize=12)
plt.ylabel('y value', fontsize=12)
plt.title('sin graph', fontsize=15)

plt.show()

x = np.arange(0, 10, 0.1)
y_1 = 1 + np.sin(x)
y_2 = 1 + np.cos(x)

sns.lineplot(x=x, y=y_1, label='1+sin', color='blue', linestyle=':')
sns.lineplot(x=x, y=y_2, label='1+cos', color='red', linestyle='-.')

plt.xlabel('x value', fontsize=15)
plt.ylabel('y value', fontsize=15)
plt.title('sin and cos graph', fontsize=18)

plt.grid()
plt.legend()

plt.show()
