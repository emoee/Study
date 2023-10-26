from IPython.display import Image
import numpy as np
import pandas as pd

from opendata import dataset
#dataset.download('서울시대중교통')
#dataset.download('서울시주민등록인구')
dataset.download('판다스입출력샘플')
dataset.download('서울시자전거')
#연습에 사용할 데이터셋 저장