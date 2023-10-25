from IPython.display import Image
import numpy as np
import pandas as pd

excel = pd.read_excel('data/seoul_transportation.xlsx', sheet_name='철도', engine='openpyxl')
print(excel.head())

#sheet_name = None 모든 데이터 읽어오기

print(excel.keys())
excel.to_excel('sample1.xlsx', index=False, sheet_name='샘플') #시트명은 생략 가능