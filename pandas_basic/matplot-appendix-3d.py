import io
from IPython.display import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
from mpl_toolkits import mplot3d
import matplotlib.image as mpimg
import urllib
from PIL import Image

warnings.filterwarnings('ignore')

# Unicode warning 제거 (폰트 관련 경고메시지)
plt.rcParams['axes.unicode_minus']=False

# 그래프 출력 사이즈 설정
plt.rcParams["figure.figsize"] = (10, 8)

fig = plt.figure()

## 3d 그래프
ax = plt.axes(projection='3d')

sample_size = 100
x = np.cumsum(np.random.normal(0, 1, sample_size))
y = np.cumsum(np.random.normal(0, 1, sample_size))
z = np.cumsum(np.random.normal(0, 1, sample_size))

ax.plot3D(x, y, z, 'gray', alpha=0.6, marker='o')
plt.title("ax.plot")
plt.show()

# Imshow
# 샘플 이미지 다운로드
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/png/img6.png'

image_data = urllib.request.urlopen(url).read()
image_stream = io.BytesIO(image_data)
image = Image.open(image_stream)

image_array = np.array(image)

plt.imshow(image)
plt.show()
